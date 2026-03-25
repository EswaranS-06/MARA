# MARA — Multi-source AI Research Assistant ⚡

MARA is a high-performance assistant built to extract deep insights from mixed data sources using state-of-the-art semantic search. It bridges the gap between your documents and your questions with a minimalist, professional interface.

---

## 🚀 Instant Setup

MARA is designed with a "One-Click Start" philosophy. Use the platform-specific scripts in the root folder to automate the entire setup (environment creation, dependency installation, and launch).

### Windows

Double-click or run:

```cmd
run_mara.bat
```

### Linux / macOS

```bash
chmod +x run_mara.sh
./run_mara.sh
```

*The scripts intelligently detect if `uv` is installed for high-speed performance; if not, they automatically fall back to standard `python/pip`.*

---

## 🧠 The Intelligence Core: How it Works

MARA utilizes a **Semantic Vector Retrieval** architecture (a specialized phase of RAG - Retrieval Augmented Generation) to understand the context of your questions rather than just matching keywords.

### 🔬 The Model

- **Engine**: `all-MiniLM-L6-v2` from Sentence-Transformers.
- **Specs**: A compact yet powerful model trained on over 1 billion sentence pairs, providing a high-dimensional semantic understanding of text.

### ⛓️ The Pipeline

1. **🔍 Ingestion**: High-fidelity text extraction from PDFs, Word documents, and Web content.
2. **🧹 Refinement**: Cleaning noise and formatting raw source data.
3. **🧱 Neural Chunking**: Breaking down data into semantically dense segments.
4. **💠 Tensor Generation**: The AI model converts segments into vector embeddings (mathematical maps of meaning).
5. **💾 Vector Vault**: Chunks are indexed in a high-speed **FAISS** (Facebook AI Similarity Search) database.
6. **🎯 Query Resolution**: When you ask a question, MARA maps it to the same vector space and finds the top "Observation Nodes" (most relevant findings) with a calculated relevance score.

---

## 📄 Supported Sources

### Currently Supported

- **PDF Intelligence**: Deep parsing for technical papers and research documents.
- **Word/DOCX**: Direct ingestion of reports and manuscripts.
- **Web URLs**: Real-time extraction from articles and online resources.

### Future Expansion

- [ ] Excel/CSV Data Analysis
- [ ] Integration with Local LLMs (Ollama/LM Studio for answer generation)
- [ ] Persistent Intelligence Vaults (Long-term data memory)

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+**: The core execution engine.
- **`uv` (Recommended)**: For ultra-fast package management and isolated environments.
- **Internet Connection**: Required for the initial download of the `all-MiniLM-L6-v2` neural model (cached locally thereafter).

---

## 📁 Project Architecture

```text
MARA/
├── backend/
│   ├── ingestion/         # PDF, Word, and Web loaders
│   ├── embeddings/        # all-MiniLM-L6-v2 implementation
│   ├── vector_store/      # FAISS indexing layer
│   ├── retrieval/         # Semantic search algorithms
│   ├── processing/        # Text cleaners & chunkers
│   └── app.py             # Main Streamlit Workspace
├── run_mara.bat           # Windows Auto-setup & Start
├── run_mara.sh            # Linux/macOS Auto-setup & Start
└── README.md              # Project Documentation
```

---

## 🤝 Contributing & Support

Contributions are what make the open-source community an amazing place to learn, inspire, and create.

1. **Fork** the Project.
2. **Create** your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. **Commit** your Changes (`git commit -m 'Add some AmazingFeature'`).
4. **Push** to the Branch (`git push origin feature/AmazingFeature`).
5. **Open** a Pull Request.

---

## 🛡️ Security & Privacy

MARA is designed with a **Privacy-First** approach:

- **Local Vectors**: All data indexing happens in memory on your local machine.
- **No Data Leakage**: Your document contents are never sent to external LLM APIs (Ollama/Local LLM integration is planned for the future for complete air-gapped local operation).

---

## ⚖️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---
*Developed for researchers who need accurate, semantically aware data retrieval at the speed of thought.*
