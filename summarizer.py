import os
import requests
from langchain_community.llms import Ollama
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain


class OllamaSummarizer:
    def __init__(self) -> None:

        LLM_NAME = os.environ.get("LLM_NAME")
        OLLAMA_HOST = os.environ.get("OLLAMA_HOST")
        LLM_BASE_URL = f"http://{OLLAMA_HOST}"

        self.llm = self.load_llm(LLM_NAME, LLM_BASE_URL)

    def load_llm(self, LLM_NAME, LLM_BASE_URL):
        # TODO: add logger
        url = f"{LLM_BASE_URL}/api/pull"
        payload = {"name": LLM_NAME}
        requests.post(url, json=payload)

        llm = Ollama(model=LLM_NAME, base_url=LLM_BASE_URL)
        return llm

    def load_docs(self, links):
        loader = WebBaseLoader(links)
        docs = loader.load()
        return docs

    def summarize_docs(self, docs):
        chain = load_summarize_chain(self.llm, chain_type="stuff")
        summary = chain.invoke(docs)
        result = summary["output_text"]
        return result


if __name__ == "__main__":

    summarizer = OllamaSummarizer()
    # TODO add cmdline parser
    links = [
        "https://towardsdatascience.com/17-types-of-similarity-and-dissimilarity-measures-used-in-data-science-3eb914d2681"
    ]
    docs = summarizer.load_docs(links)

    result = summarizer.summarize_docs(docs)
    print(result)
