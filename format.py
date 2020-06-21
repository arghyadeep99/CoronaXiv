import json
import os
import csv

def get_details(file):
    data = json.load(file)

    paper_id = data['paper_id']

    title = data['metadata']['title']

    # Abstract
    abstract_paras = len(data['abstract'])
    abstract_text = ""
    for i in range(abstract_paras):
        abstract_text += data['abstract'][i]['text']

    # Authors
    number_of_authors = len(data['metadata']['authors'])
    authors_list = []
    for i in range(number_of_authors):
        authors_list.append(data['metadata']['authors'][i]['first'] + ' ' + data['metadata']['authors'][i]['last'])
    authors = ', '.join(authors_list)

    return paper_id, title, abstract_text, authors

def main():
    DATA_DIR_PATH = '' # Path of the dataset set directory

    # Read all files in the directory
    # Columns
    cols = ['paper_id', 'title', 'abstract', 'authors', 'doi']

    with open("papers.csv", 'w', newline='', encoding="utf8") as csv_file:
        # writing to the csv
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(cols)
        count = 0
        data = json.load(open("myfile.json", "r"))
        # print(data)
        for file in data:
            print(f'{count}. is being written')
            file_path = os.path.join(DATA_DIR_PATH, file['sha'])
            # print(file_path)
            paper_id, title, abstract, authors = get_details(open(file_path), "r", encoding="utf8")
            csv_writer.writerow([paper_id, title, abstract, authors, file['doi']])      
            count += 1

main()