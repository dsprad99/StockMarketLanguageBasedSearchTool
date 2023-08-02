from flask import Flask, request, jsonify, send_from_directory
import os
import constants
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = constants.APIKEY

app = Flask(__name__)

def perform_query(query):
    try:
        # loader = TextLoader('data.txt')
        loader = TextLoader('data.txt', encoding='utf-8')
        index = VectorstoreIndexCreator().from_loaders([loader])
        results = index.query(query)
        return results
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    query = data.get('query', '')
    results = perform_query(query)
    return results

if __name__ == '__main__':
    app.run(debug=True)

