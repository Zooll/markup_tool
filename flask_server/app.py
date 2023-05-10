from flask import Flask, request
from flask_cors import CORS, cross_origin
import logging
import base64
import requests
import json

from pymongo import MongoClient

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
logging.getLogger().addHandler(logging.StreamHandler())


app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string
db = client['markuper']  # Replace with your database name
    


@app.route('/')
@cross_origin()
def index():
    # Example: Perform a MongoDB query
    collection = db['texts']  # Replace with your collection name
    documents = collection.find()
    
    # Example: Iterate over the documents and display them
    # for doc in documents:
    #     print(doc)
    
    # Convert the results to JSON format
    json_results = json.dumps([str(doc) for doc in documents])
    print(json_results)

    return json_results

if __name__ == '__main__':
    app.run(host="0.0.0.0")