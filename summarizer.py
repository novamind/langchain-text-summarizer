import os
import requests
from langchain_community.llms import Ollama
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain
from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate


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

    def get_answer(self, docs, question):

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500)
        documents = text_splitter.split_documents(docs)

        OLLAMA_HOST = os.environ.get("OLLAMA_HOST")
        embeddings = OllamaEmbeddings(base_url=f"http://{OLLAMA_HOST}")

        vector = Chroma.from_documents(documents, embeddings)
        system_prompt = (
            """
                Answer the user's questions based on the below context. 
                If the context doesn't contain any relevant information to the question, don't make something up and just say "I don't know":

                <context>
                {context}
                </context>
                """
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )

        document_chain = create_stuff_documents_chain(self.llm, prompt)
        retriever = vector.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)
        response = retrieval_chain.invoke({"input": question})

        return response


if __name__ == "__main__":

    summarizer = OllamaSummarizer()
    # TODO add cmdline parser
    links = [
        "https://towardsdatascience.com/17-types-of-similarity-and-dissimilarity-measures-used-in-data-science-3eb914d2681"
    ]
    docs = summarizer.load_docs(links)

    # result = summarizer.summarize_docs(docs)
    # print(result)
    summarizer.get_answer(docs)
