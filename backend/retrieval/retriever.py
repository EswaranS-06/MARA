class Retriever:

    def __init__(self, store, embedder):
        self.store = store
        self.embedder = embedder

    def ask(self, query: str, top_k=3):
        query_vector = self.embedder.embed([query])[0]
        results = self.store.search(query_vector, top_k)

        return results