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
    data = client.search(engine_name, query, {})
    return jsonify({'data': data})
    

# New Index Route
@app.route("/createindex")
def create_index():
    request_body = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        },
        'mappings': {
            "properties": {
              "title_x":   { "type": "text"  }     
            }
        }
    }
    es.indices.create(index='movie_index', body=request_body)
    return jsonify({ 'result': 'created' })

if __name__ == "__main__":
    app.run(debug=False)