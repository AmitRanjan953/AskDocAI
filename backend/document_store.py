import fitz  # PyMuPDF

def extract_text_from_file(filename, content):
    if filename.endswith(".pdf"):
        with open("/tmp/temp.pdf", "wb") as f:
            f.write(content)
        doc = fitz.open("/tmp/temp.pdf")
        return "\n".join([page.get_text() for page in doc])
    else:
        return content.decode("utf-8")