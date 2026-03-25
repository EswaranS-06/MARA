from docx import Document

class DocxLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> str:
        doc = Document(self.file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text