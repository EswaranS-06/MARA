from langchain_text_splitters import RecursiveCharacterTextSplitter
from core.config import CHUNK_SIZE, CHUNK_OVERLAP


class TextChunker:

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=[
                "\n\n",   # paragraphs
                "\n",     # lines
                " "       # fallback ONLY
            ]
        )

    def chunk(self, text: str):
        chunks = self.splitter.split_text(text)

        # 🔥 Post-clean chunks
        cleaned_chunks = []

        for chunk in chunks:
            chunk = chunk.strip()

            # remove leading punctuation
            chunk = chunk.lstrip(". ,")

            if len(chunk) > 50:  # ignore tiny junk chunks
                cleaned_chunks.append(chunk)

        return cleaned_chunks