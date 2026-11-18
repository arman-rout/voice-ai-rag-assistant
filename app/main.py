#This is the central connection point.

#It initializes the document pipeline, vector store, RAG service, and Gemini service.


from app.config import validate_config

from app.utils.document_loader import (
    load_documents,
    chunk_documents
)

from app.services.vector_store import VectorStore
from app.services.rag import RAGService
from app.services.llm import LLMService


class VoiceRAGAgent:

    def __init__(self):

        validate_config()

        print("Loading company documents...")

        documents = load_documents(
            "data/knowledge_base"
        )

        if not documents:
            raise ValueError("No company documents found")

        chunks = chunk_documents(documents)

        print(f"Created {len(chunks)} chunks")

        self.vector_store = VectorStore()

        self.vector_store.build_index(chunks)

        self.rag = RAGService(
            self.vector_store
        )

        self.llm = LLMService()

        print("Voice RAG agent is ready!")

    def ask(self, question):

        context, sources = self.rag.retrieve_context(
            question
        )

        if not context:

            return {
                "answer": "I could not find relevant information in the company documents.",
                "sources": []
            }

        answer = self.llm.generate_answer(
            question=question,
            context=context
        )

        return {
            "answer": answer,
            "sources": sources
        }