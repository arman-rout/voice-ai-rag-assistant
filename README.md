# Voice AI Customer Support Agent with RAG

An AI-powered voice customer support assistant that understands customer questions, retrieves relevant information from company documents using Retrieval-Augmented Generation (RAG), generates accurate answers using Google Gemini, and responds with natural-sounding speech using ElevenLabs.

The application supports both text-based and voice-based customer interactions.

---

## Project Overview

Traditional customer support systems often require human agents to answer repetitive questions.

This project provides an AI-powered customer support solution that can:

- Understand customer questions through voice or text.
- Convert speech into text using Deepgram.
- Retrieve relevant information from company documents.
- Generate context-aware responses using Google Gemini.
- Convert AI-generated answers into speech using ElevenLabs.
- Provide an interactive interface using Streamlit.

The main goal is to build an intelligent customer support assistant using Generative AI, RAG, vector search, and speech technologies.

---

## System Architecture

```text
                  CUSTOMER
                     |
              Voice / Text Input
                     |
          +----------+----------+
          |                     |
       Voice Input          Text Input
          |                     |
       Deepgram                 |
     Speech-to-Text             |
          |                     |
          +----------+----------+
                     |
                User Question
                     |
             Sentence Transformers
                 Embeddings
                     |
                FAISS Search
                     |
             Relevant Documents
                     |
                RAG Pipeline
                     |
                Google Gemini
                 LLM Response
                     |
               ElevenLabs TTS
                     |
                Audio Response
                     |
                  CUSTOMER
```

### Document Ingestion Pipeline

```text
Company PDF / TXT Documents
            |
      Document Loader
            |
       Text Extraction
            |
        Text Chunking
            |
     Sentence Transformers
            |
        Embeddings
            |
        FAISS Index
```

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | User interface |
| Google Gemini | Large Language Model |
| Sentence Transformers | Text embeddings |
| FAISS | Vector similarity search |
| Deepgram | Speech-to-Text |
| ElevenLabs | Text-to-Speech |
| Pypdf | PDF text extraction |
| HTTPX | API communication |
| Python-dotenv | Environment configuration |

---

## Project Structure

```text
voice-ai-rag/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── stt.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── rag.py
│   │   ├── llm.py
│   │   └── tts.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── document_loader.py
│
├── data/
│   └── knowledge_base/
│       └── company_info.txt
│
├── vector_db/
│
├── frontend/
│   └── ui.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd voice-ai-rag
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root directory.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GEMINI_MODEL=YOUR_SUPPORTED_GEMINI_MODEL

DEEPGRAM_API_KEY=YOUR_DEEPGRAM_API_KEY

ELEVENLABS_API_KEY=YOUR_ELEVENLABS_API_KEY
ELEVENLABS_VOICE_ID=YOUR_ELEVENLABS_VOICE_ID
```

**Important:** Never upload your `.env` file or API keys to GitHub.

Obtain API credentials:

- Gemini: https://aistudio.google.com/apikey
- Deepgram: https://console.deepgram.com/
- ElevenLabs: https://elevenlabs.io/

Check the current Gemini model IDs in the official documentation:
https://ai.google.dev/gemini-api/docs/models

### 5. Add company documents

Place your company PDF or TXT files inside:

```text
data/knowledge_base/
```

Example:

```text
data/knowledge_base/company_info.txt
```

The document loader extracts the text and prepares it for embedding and retrieval.

---

## ▶️ How to Run the Project

Run the application from the main project directory.

### Step 1: Activate virtual environment

```powershell
venv\Scripts\activate
```

### Step 2: Verify dependencies

```powershell
python -c "import streamlit, google.genai, sentence_transformers, faiss, pypdf, httpx; print('All packages working')"
```

### Step 3: Start Streamlit

```powershell
python -m streamlit run frontend/ui.py
```

### Step 4: Open the application

Open your browser:

```text
http://localhost:8501
```

The application should now display the Voice AI Customer Support interface.

---

## 🔄 Application Workflow

### 1. Document Processing

- Load company PDF and TXT files.
- Extract document content.
- Split content into smaller chunks.
- Generate vector embeddings.
- Build a FAISS vector index.

### 2. Customer Question Processing

- Receive a customer question through text or voice.
- Use Deepgram to transcribe voice input.
- Generate an embedding for the question.
- Search the FAISS index for relevant chunks.
- Retrieve relevant company information.

### 3. Answer Generation

- Pass the customer question and retrieved context to Gemini.
- Generate a natural-language answer.
- Avoid unsupported company information.

### 4. Voice Response

- Send the generated answer to ElevenLabs.
- Generate speech audio.
- Play the audio response through the application.

---

## Example Questions

Try asking:

1. What services does Tech Solutions provide?
2. What is your refund policy?
3. What are your customer support hours?
4. How much does voice AI development cost?
5. What is the starting price of chatbot development?

The answers should be based on the information available in the company knowledge base.

---

## Security

- Store API keys in `.env`.
- Never commit API credentials to GitHub.
- Include `.env` in `.gitignore`.
- Regenerate credentials if they are accidentally exposed.
- Avoid logging confidential customer information.

---

## Key Learning Outcomes

Through this project, you can demonstrate practical knowledge of:

- Generative AI and Large Language Models.
- Retrieval-Augmented Generation (RAG).
- Semantic search and vector databases.
- Text embedding models.
- Prompt engineering.
- Speech-to-Text and Text-to-Speech.
- API integration.
- Python application development.
- AI-powered customer support systems.

---

## Future Enhancements

- Real-time voice conversation.
- Conversation memory.
- Persistent FAISS index storage.
- Multiple document and knowledge-base management.
- User authentication.
- PostgreSQL conversation history.
- Redis caching.
- FastAPI backend.
- Docker deployment.
- Cloud deployment and monitoring.
- Human-agent escalation.

---

## Project Information

**Project Name:** Voice AI Customer Support Agent with RAG

**Category:** Generative AI | Voice AI | RAG | NLP

**Primary Language:** Python

**Interface:** Streamlit

**Status:** MVP Development

---
