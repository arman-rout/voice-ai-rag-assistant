"""Responsibility:
- Store document vectors in FAISS.
- Convert customer questions into vectors.
- Find the most similar document chunks."""

import faiss

from app.services.embeddings import EmbeddingService


class VectorStore:

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.index = None

        self.chunks = []

    def build_index(self, chunks):

        if not chunks:
            raise ValueError("No document chunks to index")

        self.chunks = chunks

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        vectors = self.embedding_service.create_embeddings(
            texts
        )

        dimension = vectors.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(vectors)

        print(f"FAISS index created with {len(chunks)} chunks")

    def search(self, query, top_k=3):

        if self.index is None:
            return []

        query_vector = self.embedding_service.create_embeddings(
            [query]
        )

        scores, indices = self.index.search(
            query_vector,
            min(top_k, len(self.chunks))
        )

        results = []

        for score, index in zip(scores[0], indices[0]):

            if index < 0:
                continue

            result = self.chunks[index].copy()

            result["score"] = float(score)

            results.append(result)

        return results