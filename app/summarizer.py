from langchain_community.llms import Ollama
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain

# TODO: use env variables for base_url
llm = Ollama(model="llama2", base_url="http://ollama:11434")


def load_docs(links):
    loader = WebBaseLoader(links)
    docs = loader.load()
    return docs


def summarize_docs(docs):
    chain = load_summarize_chain(llm, chain_type="stuff")
    summary = chain.invoke(docs)
    result = summary["output_text"]
    return result


if __name__ == "__main__":
    # TODO add cmdline parser
    links = [
        "https://towardsdatascience.com/17-types-of-similarity-and-dissimilarity-measures-used-in-data-science-3eb914d2681"
    ]
    docs = load_docs(links)

    result = summarize_docs(docs)
    print(result)
