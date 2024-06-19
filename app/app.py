from flask import Flask, request
from summarizer import load_docs, summarize_docs

app = Flask(__name__)


@app.route("/summarize", methods=["post"])
def get_summary():

    data = request.json
    docs = load_docs(data["urls"])
    result = summarize_docs(docs)

    return result


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
