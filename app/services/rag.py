#Responsibility: Retrieve relevant chunks and prepare context for Gemini.

class RAGService:

    def __init__(self, vector_store):

        self.vector_store = vector_store

    def retrieve_context(self, question):

        results = self.vector_store.search(
            query=question,
            top_k=3
        )

        if not results:
            return "", []

        context_parts = []

        for item in results:

            source = item["source"]

            if item.get("page"):
                source += f", page {item['page']}"

            context_parts.append(
                f"[Source: {source}]\n{item['text']}"
            )

        context = "\n\n".join(context_parts)

        return context, results