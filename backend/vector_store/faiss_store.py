import faiss
import numpy as np


class FAISSStore:

    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, vectors, texts):
        vectors = np.array(vectors).astype("float32")

        self.index.add(vectors)
        self.texts.extend(texts)

    def search(self, query_vector, top_k=3):
        query_vector = np.array([query_vector]).astype("float32")

        distances, indices = self.index.search(query_vector, top_k)

        results = []
        for i in indices[0]:
            results.append(self.texts[i])

        return results