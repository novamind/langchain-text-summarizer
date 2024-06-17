from langchain_community.llms import Ollama
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate

llm = Ollama(model="llama2")

def load_docs(links):
    loader = WebBaseLoader(links)
    docs = loader.load()
    return docs

def summarize_docs(docs):
    chain = load_summarize_chain(llm, chain_type="stuff")
    summary = chain.invoke(docs)
    result = summary['output_text']
    return result

if __name__ == "__main__":

    # links = [
    #     "https://medium.com/@social_65128/the-comprehensive-guide-to-understanding-generative-ai-c06bbf259786",
    #     "https://medium.com/@stahl950/understanding-the-basics-generative-ai-1a995f230897",
    #     "https://medium.com/educative/what-is-prompt-engineering-definition-and-best-practices-10b6523c69d5",
    #     "https://medium.com/towards-data-science/comparing-documents-with-similarity-metrics-e486bc678a7d"]
    # loader = WebBaseLoader(links)

    links = ["https://towardsdatascience.com/17-types-of-similarity-and-dissimilarity-measures-used-in-data-science-3eb914d2681"]
    docs = load_docs(links)
        
    result = summarize_docs(docs)
    print(result)