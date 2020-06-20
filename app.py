from flask import Flask, request, jsonify  
from elasticsearch import Elasticsearch

import os
import json

app = Flask(__name__)

es = Elasticsearch(
    cloud_id = os.environ.get('ELASTIC_CLOUD_ID'),
    http_auth = (os.environ.get('ELASTIC_USERNAME'), os.environ.get("ELASTIC_PASSWORD"))
)

# Index Route
@app.route("/")
def home():
    return jsonify({ 'msg': 'Welcome' })

# Search Route
@app.route("/search", methods = ['POST'])
def search():
    if request.method == 'POST':
        query = request.form['search']
        value = request.form['value']
        search_param = {
            'query': {
                'match': {
                    query: value
                }
            }
        }
        data = es.search(index="papers", body=search_param)
        print(data)
        return jsonify({'data': data})

@app.route("/title", methods = ['POST'])
def title_search():
    if request.method == 'POST':
        query = request.form['search']
        search_param = {
            'query': {
                'match': {
                    'title': query
                }
            }
        }
        data = es.search(index="papers", body=search_param)
        print(data)
        return jsonify({'data': data})

if __name__ == "__main__":
    app.run(debug=False)