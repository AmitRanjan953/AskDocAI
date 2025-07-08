# AskDocAI 🤖📄

A Smart GenAI Assistant for Research Summarization and Comprehension.

## Features

- 📤 Upload PDF/TXT files
- 📑 Auto summary (≤150 words)
- 🔍 Ask questions with contextual document-aware answers
- 🧠 Challenge Me: Logical question generation & evaluation
- ✅ Justified answers with source references

## How to Run

### Backend (FastAPI)

```bash
pip install -r requirements.txt
uvicorn backend.app:app --host 0.0.0.0 --port 8501
```

### Frontend (Streamlit)

```bash
streamlit run frontend/streamlit_app.py
```

### Requirements

```bash
pip install -r requirements.txt
```

## API Endpoints

- `POST /upload` – Upload and process document
- `POST /predict` – Ask a question from the document
- `POST /challenge` – Get logic-based questions
- `POST /evaluate` – Submit answers for evaluation

## Example

POST `/predict`
```json
{
  "question": "What causes blurry vision?"
}
```

## License

MIT © Amit Ranjan Gupt