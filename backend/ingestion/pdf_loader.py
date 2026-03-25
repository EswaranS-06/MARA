from PyPDF2 import PdfReader

class PDFLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self) -> str:
        reader = PdfReader(self.file_path)
        text = ""

        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

        return text