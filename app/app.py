from flask import Flask, request
from summarizer import load_docs, summarize_docs
app = Flask(__name__)


@app.route('/summarize', methods=['post'])
def get_summary():
    # links = ["https://towardsdatascience.com/17-types-of-similarity-and-dissimilarity-measures-used-in-data-science-3eb914d2681"]

    data = request.json
    print(data)
    docs = load_docs(data['urls'])
        
    result = summarize_docs(docs)

    return result

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)