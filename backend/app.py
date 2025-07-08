from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from backend.utils import summarize_text, answer_question, generate_logic_questions, evaluate_response
from backend.document_store import extract_text_from_file

app = FastAPI()
document_text = ""

class QARequest(BaseModel):
    question: str

class EvaluationRequest(BaseModel):
    answers: list

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    global document_text
    content = await file.read()
    document_text = extract_text_from_file(file.filename, content)
    summary = summarize_text(document_text)
    return {"summary": summary}

@app.post("/predict")
def predict(input: QARequest):
    answer, justification = answer_question(input.question, document_text)
    return {"answer": answer, "justification": justification}

@app.post("/challenge")
def challenge():
    questions = generate_logic_questions(document_text)
    return {"questions": questions}

@app.post("/evaluate")
def evaluate(data: EvaluationRequest):
    feedback = evaluate_response(data.answers, document_text)
    return {"feedback": feedback}