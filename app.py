"""
app.py
------
Streamlit UI for Research Paper Management & Analysis Intelligence System.

Features:
- Upload research papers (PDF)
- Build semantic index
- Auto-generate structured summaries
- Ask research questions using RAG (Groq LLM)
- Clean, reviewer-friendly UI
"""

import os
import uuid
import streamlit as st

from core import (
    ResearchPDFParser,
    SectionChunker,
    EmbeddingManager,
    PaperVectorStore,
    SemanticRetriever,
    PaperSummarizer,
    ResearchQAEngine,
    TrendAnalyzer,
)
from services import (
    PaperIngestionService,
    SearchService,
    AnalysisService,
)

# ----------------------------
# Streamlit Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Research Paper Intelligence",
    layout="wide",
    initial_sidebar_state="expanded",
)

if "paper_summary" not in st.session_state:
    st.session_state.paper_summary = ""

# ----------------------------
# Session State Initialization
# ----------------------------
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "papers_loaded" not in st.session_state:
    st.session_state.papers_loaded = False

if "paper_text" not in st.session_state:
    st.session_state.paper_text = ""

# ----------------------------
# Sidebar – Paper Management
# ----------------------------
st.sidebar.title("📚 Research Library")

uploaded_file = st.sidebar.file_uploader(
    "Upload Research Paper (PDF)",
    type=["pdf"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Powered by Groq + LangChain")

# ----------------------------
# Main Header
# ----------------------------
st.markdown(
    """
    <h1 style="text-align:center;">🧠 Research Paper Management & Analysis</h1>
    <p style="text-align:center; color:gray;">
    Semantic Search • Summarization • Research Q&A
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ----------------------------
# Backend Initialization
# ----------------------------
parser = ResearchPDFParser()
chunker = SectionChunker()
embedder = EmbeddingManager()

# Vector store will be created after first upload
trend_analyzer = TrendAnalyzer()

# ----------------------------
# Session State Initialization
# ----------------------------
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "papers_loaded" not in st.session_state:
    st.session_state.papers_loaded = False

if "paper_text" not in st.session_state:
    st.session_state.paper_text = ""


# ----------------------------
# Handle PDF Upload
# ----------------------------
if uploaded_file:
    if not st.session_state.papers_loaded:
        with st.spinner("📄 Processing research paper (one-time)..."):
            os.makedirs("data/raw_papers", exist_ok=True)
            paper_id = str(uuid.uuid4())[:8]
            pdf_path = f"data/raw_papers/{paper_id}.pdf"

            with open(pdf_path, "wb") as f:
                f.write(uploaded_file.read())

            # --- One-time ingestion ---
            sections = parser.extract_sections(pdf_path)

            st.session_state.paper_text = "\n\n".join(
                sec.text for sec in sections
            )

            chunks = []
            for sec in sections:
                chunks.extend(
                    chunker.chunk(paper_id, sec.section_name, sec.text)
                )

            vector_store = PaperVectorStore(embedder.model)
            vector_store.index(chunks)

            # Save once
            st.session_state.vector_store = vector_store
            st.session_state.papers_loaded = True

        st.sidebar.success("✅ Paper indexed (cached in session)")
    else:
        st.sidebar.info("📌 Paper already indexed — using cached vector store")

# ----------------------------
# Tabs Layout
# ----------------------------
tab1, tab2, tab3 = st.tabs([
    "📄 Paper Overview",
    "🧾 Auto Summary",
    "💬 Research Chat"
])

# ----------------------------
# TAB 1 – Paper Overview
# ----------------------------
with tab1:
    st.subheader("Paper Status")

    if st.session_state.papers_loaded:
        st.success("Paper successfully loaded and indexed.")
        st.info("You can now generate summaries or ask questions.")
    else:
        st.warning("Please upload a research paper to begin.")

# ----------------------------
# TAB 2 – Auto Summary
# ----------------------------
with tab2:
    st.subheader("Structured Paper Summary")

    if st.session_state.papers_loaded:

        if st.button("Generate Summary"):
            with st.spinner("🧠 Generating academic summary..."):
                summarizer = PaperSummarizer()
                st.session_state.paper_summary = summarizer.summarize(
                    st.session_state.paper_text[:8000]
                )

        # 🔑 ALWAYS render from session_state
        if st.session_state.paper_summary:
            st.success("Summary Generated")
            st.write(st.session_state.paper_summary)

    else:
        st.warning("Upload a paper first.")


# ----------------------------
# TAB 3 – Research Chat (RAG)
# ----------------------------
with tab3:
    st.subheader("Ask Questions About the Paper")

    if st.session_state.papers_loaded:
        query = st.text_input(
            "Enter your research question",
            placeholder="e.g. What problem does this paper solve?"
        )

        if st.button("Ask"):
            with st.spinner("🔍 Retrieving evidence & generating answer..."):
                retriever = SemanticRetriever(
                    st.session_state.vector_store
                )
                qa_engine = ResearchQAEngine(retriever)
                answer = qa_engine.answer(query)

            st.markdown("### ✅ Answer")
            st.write(answer)
    else:
        st.warning("Upload a paper to enable research Q&A.")


# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption(
    "© Research Paper Management & Analysis Intelligence System | Built with Groq"
)
