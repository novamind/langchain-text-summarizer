import streamlit as st
from summarizer import OllamaSummarizer


@st.cache_resource
def get_summarizer():
    return OllamaSummarizer()


summarizer = get_summarizer()
st.title("🦜🔗 Content Assistant")

url = st.text_area("Enter a link:", "https://example.com")
st.header("Summarization")
with st.form("my_form"):

    submitted = st.form_submit_button("Summarize")
    if submitted:
        with st.spinner("Summarizing..."):
            docs = summarizer.load_docs(url)
            result = summarizer.summarize_docs(docs)
            st.success("Done!")
            st.markdown(result)

st.header("Question Answering")
with st.form("my_form2"):
    # TODO: load docs only once
    docs = summarizer.load_docs(url)
    question = st.text_area(
        "Ask a question:",
        "What is this website about?"
    )
    asked = st.form_submit_button("Ask")
    if asked:
        with st.spinner("Answering..."):
            response = summarizer.get_answer(docs, question)
            st.success("Done!")
            st.markdown(response["answer"])
