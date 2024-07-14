from flask import Flask, request
from summarizer import OllamaSummarizer

app = Flask(__name__)
summarizer = OllamaSummarizer()


@app.route("/summarize", methods=["post"])
def get_summary():

    data = request.json
    docs = summarizer.load_docs(data["urls"])
    result = summarizer.summarize_docs(docs)

    return result


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
