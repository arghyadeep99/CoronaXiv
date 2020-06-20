from flask import Flask, render_template, request, jsonify  
from elasticsearch import Elasticsearch

import os
import json

app = Flask(__name__, static_folder = "./dist/static",
            template_folder = "./dist")

es = Elasticsearch(
    cloud_id = os.environ.get('ELASTIC_CLOUD_ID'),
    http_auth = (os.environ.get('ELASTIC_USERNAME'), os.environ.get("ELASTIC_PASSWORD"))
)

@app.route("/")
def home():
    # data = client.search(engine_name, "", {})
    return render_template("home.html")

@app.route("/search", methods = ['POST'])
def search():
    if request.method == 'POST':
      query = request.form['search']
    data = client.search(engine_name, query, {})
    return render_template("results.html" , data=data)

# Create a new index
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

@app.route("/index")
def index():
    # Opening JSON file 
    f = open('data.json',) 

    # returns JSON object as  
    # a dictionary 
    documents = json.load(f)
    print(documents)
    data = es.index("movie_index", documents)
    return render_template("about.html" , data=data)

if __name__ == "__main__":
    app.run(debug=False)