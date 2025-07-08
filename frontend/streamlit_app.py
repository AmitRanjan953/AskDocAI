import streamlit as st
import requests

st.set_page_config(page_title="AskDocAI", layout="wide")
st.title("📄 AskDocAI - Smart Assistant for Research Summarization")

api_url = "http://34.67.17.138:8501"

if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

uploaded_file = st.file_uploader("Upload a PDF or TXT document", type=["pdf", "txt"])
if uploaded_file and st.button("Submit Document"):
    files = {"file": uploaded_file.getvalue()}
    res = requests.post(f"{api_url}/upload", files=files)
    if res.status_code == 200:
        st.success("Document processed.")
        st.session_state.uploaded = True
        st.session_state.summary = res.json()["summary"]

if st.session_state.uploaded:
    st.subheader("📑 Document Summary")
    st.write(st.session_state.summary)

    mode = st.radio("Choose Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        q = st.text_input("Enter your question")
        if st.button("Get Answer"):
            res = requests.post(f"{api_url}/predict", json={"question": q})
            result = res.json()
            st.markdown(f"**Answer:** {result['answer']}")
            st.markdown(f"**Justification:** {result['justification']}")

    elif mode == "Challenge Me":
        if st.button("Start Challenge"):
            res = requests.post(f"{api_url}/challenge")
            questions = res.json()["questions"]
            user_answers = []
            for i, q in enumerate(questions):
                ans = st.text_input(f"Q{i+1}: {q}")
                user_answers.append(ans)

            if st.button("Submit Answers"):
                res = requests.post(f"{api_url}/evaluate", json={"answers": user_answers})
                feedback = res.json()["feedback"]
                for fb in feedback:
                    st.markdown(f"**Q:** {fb['question']}  
**Your Answer:** {fb['your_answer']}  
**Feedback:** {fb['feedback']}")