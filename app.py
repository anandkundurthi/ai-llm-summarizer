import streamlit as st
import requests

st.set_page_config(page_title="AI Summarizer", page_icon="🤖")

st.title("🤖 AI Text Summarizer")
st.caption("Built using FastAPI + OpenAI + Streamlit")

st.write("Paste your text below and get a summary instantly.")

# Input box
text = st.text_area("Enter your text here:")

if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        with st.spinner("Generating summary..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/summarize",
                    json={"text": text}
                )

                result = response.json()

                st.subheader("📌 Summary:")
                st.write(result["summary"])

            except Exception as e:
                st.error(f"Error: {e}")
