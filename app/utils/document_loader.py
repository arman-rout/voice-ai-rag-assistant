from pathlib import Path
from pypdf import PdfReader


def load_documents(folder_path):
    documents = []

    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    for file_path in folder.glob("*"):

        if file_path.suffix.lower() == ".txt":

            text = file_path.read_text(encoding="utf-8")

            if text.strip():
                documents.append({
                    "text": text,
                    "source": file_path.name
                })

        elif file_path.suffix.lower() == ".pdf":

            reader = PdfReader(str(file_path))

            for page_number, page in enumerate(reader.pages, start=1):

                text = page.extract_text() or ""

                if text.strip():
                    documents.append({
                        "text": text,
                        "source": file_path.name,
                        "page": page_number
                    })

    return documents


def chunk_documents(documents, chunk_size=800, overlap=150):

    chunks = []

    for document in documents:

        text = document["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end].strip()

            if chunk_text:

                chunks.append({
                    "text": chunk_text,
                    "source": document["source"],
                    "page": document.get("page")
                })

            if end >= len(text):
                break

            start = end - overlap

    return chunks