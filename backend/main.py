from ingestion.url_loader import URLLoader
from processing.cleaner import TextCleaner
from processing.chunker import TextChunker
from embeddings.embedder import Embedder
from vector_store.faiss_store import FAISSStore
from retrieval.retriever import Retriever


def run_mara():
    url = "https://en.wikipedia.org/wiki/SQL_injection"

    loader = URLLoader(url)
    raw_text = loader.load()

    cleaner = TextCleaner()
    clean_text = cleaner.clean(raw_text)

    chunker = TextChunker()
    chunks = chunker.chunk(clean_text)

    embedder = Embedder()
    vectors = embedder.embed(chunks)

    store = FAISSStore(dim=vectors.shape[1])
    store.add(vectors, chunks)

    retriever = Retriever(store, embedder)

    while True:
        query = input("\nAsk something (or 'exit'): ")

        if query.lower() == "exit":
            break

        results = retriever.ask(query)

        print("\n📌 Answer:\n")
        for res in results:
            print(f"- {res}\n")


if __name__ == "__main__":
    run_mara()