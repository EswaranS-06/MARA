# MARA — Multi-source AI Research Assistant ⚡

MARA is a professional, high-performance AI research tool designed for deep insights from diverse data sources. It features the **Obsidian Glow** UI—a custom-styled intelligence command center that provides a modern, immersive research experience.

---

## ✨ Key Features

- **🌑 Obsidian Glow UI**: A premium, glassmorphic interface with radial gradients and futuristic accent glows.
- **📄 Multi-Source Intelligence**: Seamlessly ingest and analyze:
  - **PDF Documents** (Academic papers, technical reports)
  - **DOCX Files** (Business reports, draft manuscripts)
  - **Web URLs** (Live articles, online documentation)
- **🔍 Neural Vector Search**: Powered by `all-MiniLM-L6-v2` embeddings and `FAISS` for lightning-fast, highly accurate context retrieval.
- **💬 Intelligence Chat**: Interact with your data using a centered, focused chat interface with integrated observation nodes.
- **🛡️ Clean & Professional**: Features custom CSS for glassmorphism, high-contrast layouts, and sleek micro-animations.

---

## 🛠️ Tech Stack

- **UI Framework**: [Streamlit](https://streamlit.io/) with heavy custom CSS overrides.
- **NLP & Embeddings**: [Sentence-Transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`).
- **Vector Core**: [FAISS](https://github.com/facebookresearch/faiss) (Facebook AI Similarity Search).
- **Extraction Layers**:
  - `PyPDF2` / `python-docx` for document parsing.
  - `Requests` & `BeautifulSoup` for web scraping.
- **Environment**: Managed with `uv` for high-performance dependency resolution.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- `uv` (recommended) or `pip`

### Installation & Running (Automated)

MARA comes with smart auto-setup scripts for all platforms. These scripts intelligently detect if **`uv`** is installed. If so, they use it for high-performance execution; otherwise, they automatically fall back to standard `python/pip` without any manual intervention.

**Windows:**
1. Run **`run_mara.bat`** from the root folder.
   
**Linux:**
1. Grant permissions: `chmod +x run_mara.sh`
2. Run: `./run_mara.sh`

---

### Manual Setup (Optional)

If you prefer manual control:

1. **Install dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Launch**:
   ```bash
   streamlit run app.py
   ```

---

## 🎨 Creative Theme: "Obsidian Glow"

MARA isn't just a research tool—it's an experience. The "Obsidian Glow" theme features:

- **Radial Depth**: A deep space background that creates a sense of focus.
- **Holographic Bubbles**: Your questions and MARA's findings are styled with subtle neon glow.
- **Intelligence Terminal**: A sidebar console displaying real-time neural engine status.

---

## 📁 Project Structure

```text
MARA/
├── backend/
│   ├── ingestion/         # Document and URL loaders
│   ├── embeddings/        # Embedding generation logic
│   ├── vector_store/      # FAISS vector database wrapper
│   ├── retrieval/         # Retrieval & search algorithm
│   ├── processing/        # Text cleaning and chunking
│   ├── app.py             # Main Obsidian Glow Interface
│   └── main.py            # CLI implementation (if any)
└── README.md              # Project documentation
```

---

## 🛡️ Security & Privacy

MARA is designed with local processing in mind. Your documents remain yours, and the vector store is cached locally in memory for maximum speed and security.

---

## 🔮 Future Roadmap

- [ ] Support for Excel/CSV data.
- [ ] Integration with local LLMs (Ollama/LM Studio).
- [ ] Multi-document persistent storage.
- [ ] Source-level citation highlighters.

---
*Created with ❤️ by Antigravity for the next generation of researchers.*
