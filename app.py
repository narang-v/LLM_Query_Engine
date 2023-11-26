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
