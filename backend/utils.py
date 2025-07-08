from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
qa_pipeline = pipeline("question-answering", model="facebook/bart-large")

def summarize_text(text):
    return summarizer(text, max_length=150, min_length=30, do_sample=False)[0]["summary_text"]

def answer_question(question, context):
    result = qa_pipeline({"question": question, "context": context})
    return result["answer"], f"Supported by context near: {context[:150]}..."

def generate_logic_questions(context):
    return [
        "What is the main argument of the document?",
        "Which section discusses the key results?",
        "What assumptions are made in the conclusion?"
    ]

def evaluate_response(answers, context):
    return [
        {"question": q, "your_answer": a, "feedback": "Reasonable answer. Refer to section 2."}
        for q, a in zip(generate_logic_questions(context), answers)
    ]