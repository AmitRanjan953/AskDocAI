 AskDocAI 💻

A Smart GenAI Assistant for Research Summarization and Comprehension — built as part of the EZ Intern GenAI Task.

---
✅ Features 

- 📤 Upload PDF/TXT files
- 📑 Auto summary (≤150 words)
- 🔍 Ask questions with contextual, document-aware answers
- 🧠 Challenge Me: Logic-based question generation & evaluation
- ✅ Justified answers with document reference

---
 ⚙️ How to Run Locally

1. Clone the Repo

```bash
git clone https://github.com/AmitRanjan953/AskDocAI.git
cd AskDocAI


2. Set up Environment
python -m venv venv
.\venv\Scripts\activate          


3. Install Requirements
pip install -r requirements.txt


4. Start Backend (FastAPI)

$env:PYTHONPATH="."
uvicorn backend.app:app --host 127.0.0.1 --port 8501
Test: http://127.0.0.1:8501/docs

5. Start Frontend (Streamlit)
(In a second terminal:)

.\venv\Scripts\activate
streamlit run frontend/streamlit_app.py
Open: http://localhost:8502


🔁 API Endpoints
Endpoint	Method	Description
/upload	POST	Upload PDF/TXT
/predict	POST	Ask a question
/challenge	POST	Generate logic questions
/evaluate	POST	Submit answers for evaluation

 Author
Amit Ranjan Gupt
B.Tech CSE (AI & ML)
Raj Kumar Goel Institute of Technology, Ghaziabad
GitHub: @AmitRanjan953

