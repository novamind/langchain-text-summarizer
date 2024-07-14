import streamlit as st
from summarizer import OllamaSummarizer

st.title("🦜🔗 Content Summarizer")
with st.form("my_form"):
    url = st.text_area(
        "Enter a link:",
        "https://example.com",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        summarizer = OllamaSummarizer()
        docs = summarizer.load_docs(url)
        result = summarizer.summarize_docs(docs)
        st.markdown(result)
