import csv
from os.path import abspath, join, dirname, exists
from os.environ import get
import tqdm
import urllib3
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk

DATASET_PATH = join(dirname(abspath(__file__)), "papers.csv")
CHUNK_SIZE = 16384

def create_index(client, index_name):
    """Creates an index in Elasticsearch if one isn't already there."""
    client.indices.create(
        index=index_name,
        body={
            "settings": {"number_of_shards": 1},
            "mappings": {
                "properties": {
                    "paper_id": {"type": "keyword"},
                    "title": {"type": "text"},
                    "abstract": {"type": "text"},
                    "author": {"type": "text"},
                }
            },
        },
        ignore=400,
        timeout=30
    )


def generate_actions():
    """Reads the file through csv.DictReader() and for each row
    yields a single document. This function is passed into the bulk()
    helper to create many documents in sequence.
    """
    with open(DATASET_PATH, mode="r", encoding="utf8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            doc = {
                "_id": row["paper_id"],
                "paper_id": row["paper_id"],
                "title": row["title"],
                "abstract": row["abstract"],
                "authors": row["authors"],
            }

            yield doc


def main():
    print("Loading dataset...")
    number_of_docs = 0
    with open(DATASET_PATH, encoding="utf8") as f:
        number_of_docs = sum([1 for _ in f]) - 1
    print(f'{number_of_docs} loaded.....')

    client = Elasticsearch(
        cloud_id=get("ELASTIC_CLOUD_ID"),
        http_auth=(get('ELASTIC_USERNAME'), get("ELASTIC_PASSWORD")),
    )
    print("Creating an index...")
    index_name = "papers"
    create_index(client, index_name)

    print("Indexing documents...")
    progress = tqdm.tqdm(unit="docs", total=number_of_docs)
    successes = 0
    for ok, action in streaming_bulk(
        client=client, index=index_name, actions=generate_actions(),
    ):
        progress.update(1)
        successes += ok
    print("Indexed %d/%d documents" % (successes, number_of_docs))


if __name__ == "__main__":
    main()