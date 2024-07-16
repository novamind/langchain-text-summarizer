import streamlit as st
from summarizer import OllamaSummarizer


@st.cache_resource
def get_summarizer():
    return OllamaSummarizer()


summarizer = get_summarizer()
st.title("🦜🔗 Content Summarizer")
with st.form("my_form"):
    url = st.text_area(
        "Enter a link:",
        "https://example.com",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        with st.spinner("Summarizing..."):
            docs = summarizer.load_docs(url)
            result = summarizer.summarize_docs(docs)
            st.success("Done!")
            st.markdown(result)
