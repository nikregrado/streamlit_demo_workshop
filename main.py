import streamlit as st
from langchain_general import vectordbqa

with st.form("qa_form"):
    query = st.text_input('Question to your document', '')

    submitted = st.form_submit_button("Submit")

if submitted:
    result = vectordbqa(query)

    answer, citation = st.columns(2)

    with answer:
        st.header("### Answer")
        st.write(result["result"])

    with citation:
        st.header("### Citation")
        for document in result["source_documents"]:
            st.write(document.page_content)
            st.markdown("---")