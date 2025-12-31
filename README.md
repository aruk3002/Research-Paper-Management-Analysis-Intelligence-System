# 🧠 Research Paper Management & Analysis Intelligence System (GA03)

This project implements an **AI-assisted research paper management system** that helps users **ingest, analyze, and interact with academic research papers** using **semantic search** and **Retrieval-Augmented Generation (RAG)**.

The system is developed according to the **GA03 project specification** and focuses on improving **research paper understanding, discovery, and analysis**.

APP LINK - [https://research-paper-management-analysis-intelligence-system-aruk.streamlit.app](https://research-paper-management-analysis-intelligence-system-aruk.streamlit.app)

<img width="1860" height="879" alt="image" src="https://github.com/user-attachments/assets/e28300e0-163f-48e4-99cb-336b2e8a0a21" />

---

## 🎯 Project Objectives

The objectives of this system are to:

* Ingest academic research papers in PDF format
* Extract structured content from research papers
* Enable semantic search across paper content
* Generate structured summaries of papers
* Answer research questions grounded in paper content
* Track citation relationships and analyze research trends
* Provide an interactive interface for researchers

---

## 🔍 Key Functionalities

### 📄 1. Research Paper Ingestion

* Upload research paper PDFs
* Extract text from major academic sections:

  * Abstract
  * Introduction
  * Methods
  * Results
  * Conclusion
  * References

### 🔎 2. Semantic Indexing & Search

* Section-aware text chunking
* Sentence-transformer embeddings
* FAISS-based vector search for semantic retrieval

### 🧾 3. Automatic Paper Summarization

* Generates structured summaries covering:

  * Problem statement
  * Proposed approach
  * Key contributions
  * Results
  * Limitations

### 💬 4. Context-Aware Question Answering (RAG)

* Uses semantic retrieval to fetch relevant paper sections
* Answers are generated strictly from retrieved content
* Groq LLM is used for response generation

### 🔗 5. Citation Tracking

* Maintains citation relationships between papers
* Supports basic related-work analysis

### 📊 6. Research Trend Analysis

* Keyword frequency analysis across papers
* Publication year distribution analysis

### 🖥 7. Interactive User Interface

* Streamlit-based interface
* Tabs for overview, summary, and Q&A
* Cached document processing to avoid repeated computation

---

## 🏗️ System Architecture (High-Level)

```
Streamlit UI
   ↓
Service Layer (Ingestion, Search, Analysis)
   ↓
Core Logic (Chunking, FAISS, RAG, Analytics)
   ↓
External Services (Groq LLM, Embedding Models)
```

---

## 📁 Project Structure

```
research-paper-intelligence/
│
├── core/                               # Core domain logic (SOLID)
│   ├── __init__.py
│   ├── models.py                       # Data schemas
│   ├── pdf_parser.py                   # PDF → structured sections
│   ├── metadata_extractor.py           # Title, authors, year
│   ├── chunking.py                     # Section-aware chunking
│   ├── embeddings.py                   # Embedding manager
│   ├── vector_store.py                 # FAISS index handling
│   ├── retrieval.py                    # Semantic retrieval
│   ├── llm_factory.py                  # Groq LLM initialization
│   ├── summarizer.py                   # Paper summarization
│   ├── qa_engine.py                    # RAG Q&A
│   ├── citation_graph.py               # Citation relationships
│   └── trend_analyzer.py               # Research trend analysis
│
├── services/                           # Application workflows
│   ├── __init__.py
│   ├── ingestion_service.py            # PDF → FAISS pipeline
│   ├── search_service.py               # Discovery & filtering
│   └── analysis_service.py             # Summaries, QA, trends
│
├── config/                             # Central configuration
│   ├── __init__.py
│   └── settings.py
│
├── data/
│   ├── raw_papers/                     # Uploaded PDFs
│   └── faiss_index/                    # Persisted vector store
│
├── .env                                # 🔐 Groq API key (ignored)
├── .env.example                        # Sample env file
├── .gitignore
├── requirements.txt
├── app.py                              # Streamlit frontend
├── main.py                             # Backend entry point
└── README.md

```

---

## ⚙️ Technology Stack

| Component            | Technology            |
| -------------------- | --------------------- |
| Programming Language | Python                |
| LLM                  | Groq (LLaMA 3)        |
| Orchestration        | LangChain             |
| Vector Database      | FAISS                 |
| Embeddings           | Sentence Transformers |
| UI Framework         | Streamlit             |
| PDF Parsing          | PyPDF                 |

---

## 🛠️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Running the Application

```bash
streamlit run ui/app.py
```

---

## 🔄 Usage Workflow

1. Upload a research paper PDF
2. Allow the system to process and index the paper
3. Generate a structured summary
4. Ask research-related questions
5. Explore trends and citation relationships

The system avoids reprocessing documents during UI interactions by caching indexed data.

---

## 🧪 Evaluation Scope

This system supports evaluation scenarios such as:

* Quickly understanding a new research paper
* Searching for relevant sections within a paper
* Asking focused technical or conceptual questions
* Identifying recurring research themes

---

## ⚠️ Limitations

* Optimized for single-paper interaction per session
* Citation extraction is based on reference text only
* Trend analysis is keyword-based rather than topic-model driven

---

## 🚀 Future Enhancements

* Multi-paper library management
* Cross-paper comparison
* Citation network visualization
* Persistent storage for summaries and chat history


This version is **clean, balanced, and explains only what actually exists**.

