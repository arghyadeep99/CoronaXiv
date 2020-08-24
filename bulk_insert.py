import csv
import sys
from os.path import abspath, join, dirname, exists
# from os.environ import get
import tqdm
import urllib3
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk

DATASET_PATH = join(dirname(abspath(__file__)), "metadata.csv") # Dataset
# CHUNK_SIZE = 16384
csv.field_size_limit(1000000000)

def create_index(client, index_name):
    """Creates an index in Elasticsearch if one isn't already there."""
    client.indices.create(
        index=index_name,
        body={
            "settings": {"number_of_shards": 1},
            "mappings": {
                "properties": {
                    "paper_id": {"type": "keyword"},
                    "abstract": {"type": "text"},
                    "body_text": {"type": "text"},
                    "authors": {"type": "keyword"},
                    "title": {"type": "text"},
                    "journal": {"type": "keyword"},
                    "publish_time": {"type": "text"},
                    "doi": {"type": "text"},
                    "source_x": {"type": "text"},
                    "url": {"type": "text"},
                    "is_covid": {"type": "boolean"},
                    "score": {"type": "double"},
                    "readers_count": {"type": "integer"},
                    "cited_by_posts_count": {"type": "integer"},
                    "cited_by_tweeters_count": {"type": "integer"},
                    "cited_by_fbwalls_count": {"type": "integer"},
                    "cited_by_wikipedia_count": {"type": "integer"},
                    "subjects": {"type": "keyword"},
                    "peer_reviewed": {"type": "text"},
                    "excerpt": {"type": "text"},
                    "x1": {"type": "double"},
                    "x2": {"type": "double"},
                    "cluster": {"type": "integer"},
                    "keywords": {"type": "keyword"},
                    "h_index": {"type": "integer"},
                    "cluster_name": {"type":"text"}
                }
            },
        },
        ignore=400,
        timeout=300
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
                "abstract": row["abstract"],
                "body_text": row["body_text"],
                "authors": row["authors"],
                "title": row["title"],
                "journal": row["journal"],
                "publish_time": row["publish_time"],
                "doi": row["doi"],
                "source_x": row["source_x"],
                "url": row['url'],
                "is_covid": row['is_covid'],
                "score": row['score'],
                "readers_count": row['readers_count'],
                "cited_by_posts_count": row['cited_by_posts_count'],
                "cited_by_tweeters_count": row['cited_by_tweeters_count'],
                "cited_by_fbwalls_count": row['cited_by_fbwalls_count'],
                "cited_by_wikipedia_count": row['cited_by_wikipedia_count'],
                "subjects": row['subjects'],
                "peer_reviewed": row['peer_reviewed'],
                "excerpt": row['excerpt'],
                "x1": row['x1'],
                "x2": row['x2'],
                "cluster": row['cluster'],
                "keywords": row['keywords'],
                "h_index": row['h_index'],
                "cluster_name": row['cluster_name']
            }

            yield doc


def main():
    print("Loading dataset...")
    number_of_docs = 0
    with open(DATASET_PATH, encoding="utf8") as f:
        number_of_docs = sum([1 for _ in f]) - 1
    print(f'{number_of_docs} loaded.....')

    # Insert your credentials
    client = Elasticsearch(
        cloud_id='coronaxiv:YXNpYS1zb3V0aDEuZ2NwLmVsYXN0aWMtY2xvdWQuY29tJGNlZTVkOWQ3OWUxMjRjNDE5NTI0YjVlYWYzNjJlZTc2JGEyMzRmMjgyYjliYTRkMzU4NmE2OGRmNDQ2YmQzMzEw',
        http_auth=('elastic', 'RuAXbFdIGOw2Is2hMndkh8yk'),  # Username and password of elastic search        
        timeout=60
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