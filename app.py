# This file is the Frontend Application that creates a local host server in the machine.
# The URL http://127.0.0.1:5000/ displays the query search engine.
# You can here enter your query and the search results will be displayed in the tabular format
# This file uses the llm_searcher functionality from "search_main.py" to generate results of the entered query.
#Libraries import
from flask import Flask, render_template, request, jsonify
from search_main import LLMSearcher
import os

app = Flask(__name__)

COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "bb-chaabi")

# Our LLM Searcher called here for the search action
llm_searcher = LLMSearcher(collection_name=COLLECTION_NAME)


@app.route('/')
def index():
    # frontend html template
    return render_template('index.html')

@app.route('/search_startup')
def search_startup():
    q = request.args.get('q', '')
    # search results from the LLM searcher on a query 'q'
    result = llm_searcher.search(text=q)
    # returning the results in json
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
