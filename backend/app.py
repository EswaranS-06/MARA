import streamlit as st
import os
import time
import base64
from pathlib import Path

from ingestion.pdf_loader import PDFLoader
from ingestion.docx_loader import DocxLoader
from ingestion.url_loader import URLLoader

from processing.cleaner import TextCleaner
from processing.chunker import TextChunker

from embeddings.embedder import Embedder
from vector_store.faiss_store import FAISSStore
from retrieval.retriever import Retriever

# --- Page Configuration ---
st.set_page_config(
    page_title="MARA | Obsidian Glow",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Function to load local image and return base64 string
def get_image_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Try to find the generated logo
logo_path = None
for file in Path(r"C:\Users\eswar\.gemini\antigravity\brain\9d275c62-613c-42e0-94bc-df29ebd68252").glob("mara_logo_*.png"):
    logo_path = str(file)
    break

# --- Premium Obsidian Glow CSS ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

    :root {{
        --bg-color: #050505;
        --sidebar-bg: rgba(15, 15, 15, 0.8);
        --accent-purple: #8E2DE2;
        --accent-blue: #4A00E0;
        --text-color: #F0F0F0;
        --glass-bg: rgba(255, 255, 255, 0.05);
        --glass-border: rgba(255, 255, 255, 0.1);
    }}

    .stApp {{
        background: radial-gradient(circle at 50% 50%, #1a1a2e 0%, #050505 100%);
        color: var(--text-color);
        font-family: 'Outfit', sans-serif;
    }}

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {{
        background: var(--sidebar-bg) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid var(--glass-border);
        width: 350px !important;
    }}

    /* Main Chat Layout */
    .chat-container {{
        max-width: 800px;
        margin: 0 auto;
        padding-bottom: 100px;
    }}

    /* Message Bubbles */
    .stChatMessage {{
        background-color: transparent !important;
        border: none !important;
    }}

    .user-bubble {{
        background: linear-gradient(135deg, var(--accent-purple), var(--accent-blue));
        border-radius: 20px 20px 0 20px;
        padding: 1rem 1.5rem;
        margin-left: auto;
        width: fit-content;
        max-width: 80%;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        color: white;
    }}

    .ai-bubble {{
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
        backdrop-filter: blur(10px);
        border-radius: 20px 20px 20px 0;
        padding: 1.5rem;
        margin-right: auto;
        width: 100%;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }}

    /* Result Cards */
    .result-card {{
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 1.2rem;
        margin-top: 1rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    
    .result-card:hover {{
        background: rgba(255, 255, 255, 0.07);
        border-color: var(--accent-purple);
        transform: scale(1.02);
    }}

    .result-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.8rem;
    }}

    .badge {{
        background: rgba(142, 45, 226, 0.2);
        color: #D3B3FF;
        padding: 4px 12px;
        border-radius: 100px;
        font-size: 0.75rem;
        font-weight: 600;
        border: 1px solid rgba(142, 45, 226, 0.3);
    }}

    /* Animation */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    .fade-in {{
        animation: fadeIn 0.5s ease-out forwards;
    }}

    /* Hide Streamlit Decorations */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{background: transparent !important;}}

    /* Chat Input Styling - Glassmorphism Footer */
    div[data-testid="stChatInput"] {{
        background-color: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        margin-bottom: 30px !important;
        padding-top: 10px !important;
    }}
    
    div[data-testid="stChatInput"] textarea {{
        color: white !important;
    }}

    /* Universal Text Visibility */
    .stApp, p, span, div, li {{
        color: #DDE !important;
    }}
    
    h1, h2, h3, h4 {{
        color: #FFF !important;
    }}
</style>
""", unsafe_allow_html=True)

# --- App Content ---

# Sidebar Content
with st.sidebar:
    if logo_path:
        st.image(logo_path, use_container_width=True)
    else:
        st.title("MARA ⚡")
    
    st.markdown("""
    <div style="padding: 10px; border-radius: 12px; border: 1px solid rgba(142,45,226,0.3); background: rgba(142,45,226,0.05); margin-bottom: 20px;">
        <p style="color: #D3B3FF; font-size: 0.8rem; margin: 0; font-family: 'Courier New', Courier, monospace;">
            > SYSTEM_LINK_ESTABLISHED<br>
            > VAULT_SECURE_MODE: ON<br>
            > NEURAL_ENGINE: IDLE
        </p>
    </div>
    """, unsafe_allow_html=True)
        
    st.markdown("### 🌑 Obsidian Controls")
    
    source_type = st.radio(
        "Intelligence Vector:",
        ["PDF Document", "DOCX Report", "Web URL"],
        help="Select the source for MARA to analyze."
    )
    
    uploaded_file = None
    url_input = None
    
    if "PDF" in source_type:
        uploaded_file = st.file_uploader("Upload PDF Intelligence", type=["pdf"])
    elif "DOCX" in source_type:
        uploaded_file = st.file_uploader("Upload DOCX Intelligence", type=["docx"])
    else:
        url_input = st.text_input("Ingest URL", placeholder="https://research-portal.com")
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("Initialize MARA"):
        process_type = "PDF" if "PDF" in source_type else ("DOCX" if "DOCX" in source_type else "URL")
        if (uploaded_file or url_input):
            try:
                with st.status("🔮 Accessing Intelligence Layer...", expanded=True) as status:
                    if process_type == "PDF":
                        with open("temp.pdf", "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        loader = PDFLoader("temp.pdf")
                    elif process_type == "DOCX":
                        with open("temp.docx", "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        loader = DocxLoader("temp.docx")
                    else:
                        loader = URLLoader(url_input)
                    
                    st.write("🌌 Extracting core patterns...")
                    raw_text = loader.load()
                    
                    st.write("🎭 Filtering noise...")
                    cleaner = TextCleaner()
                    clean_text = cleaner.clean(raw_text)
                    
                    st.write("🧱 Reconstructing neural blocks...")
                    chunker = TextChunker()
                    chunks = chunker.chunk(clean_text)
                    
                    st.write("💠 Generating vector embeddings...")
                    embedder = Embedder()
                    vectors = embedder.embed(chunks)
                    
                    st.write("💾 Finalizing Obsidian Vault...")
                    store = FAISSStore(dim=vectors.shape[1])
                    store.add(vectors, chunks)
                    
                    st.session_state.retriever = Retriever(store, embedder)
                    st.session_state.processed = True
                    status.update(label="Initialization Complete!", state="complete", expanded=False)
                
                st.balloons()
                
                if os.path.exists("temp.pdf"): os.remove("temp.pdf")
                if os.path.exists("temp.docx"): os.remove("temp.docx")
            except Exception as e:
                st.error(f"Neural Error: {e}")
        else:
            st.warning("Please provide a valid intelligence source.")

    st.markdown("---")
    # Fancy Status
    if st.session_state.get("processed", False):
        st.success("🟢 MARA ACTIVE")
    else:
        st.info("⚪ MARA DORMANT")

    if st.button("Purge History"):
        st.session_state.messages = []
        st.rerun()

# --- Main Interaction Logic ---

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Centered Header
st.markdown("<div style='text-align: center; padding: 2rem 0;'>", unsafe_allow_html=True)
st.markdown("<h1 style='font-size: 3rem; background: linear-gradient(to right, #8E2DE2, #4A00E0); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>MARA Intelligence Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #888; font-size: 1.1rem;'>Ask deep questions from your documents and web data.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Chat Display Container
chat_placeholder = st.container()

with chat_placeholder:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-bubble fade-in">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            # Assistant Response
            ai_content = f'<div class="ai-bubble fade-in">'
            ai_content += f'<p style="margin-bottom: 1rem; opacity: 0.7;">Extracted findings for: <i>"{message["query"]}"</i></p>'
            
            for i, res in enumerate(message["results"]):
                relevance = 99 - (i * 3)
                # Ensure the text is escaped for HTML and not broken by markdown parser
                safe_res = res.replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")
                card_html = f'<div class="result-card"><div class="result-header"><span style="font-weight: 600; color: #FFF;">Observation node {i+1}</span><span class="badge">Relevance: {relevance}%</span></div><div style="color: #DDD; font-size: 0.95rem; line-height: 1.6;">{safe_res}</div></div>'
                ai_content += card_html
            
            ai_content += '</div>'
            st.markdown(ai_content, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# Bottom Spacer for fixed input
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

# Chat Input at bottom
if prompt := st.chat_input("Query the Obsidian Vault...", disabled=not st.session_state.get("processed", False)):
    # Append User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Process with Retriever
    with st.spinner("Searching neural pathways..."):
        time.sleep(0.4) # Aesthetic delay
        results = st.session_state.retriever.ask(prompt)
        
        st.session_state.messages.append({
            "role": "assistant",
            "query": prompt,
            "results": results
        })
    
    st.rerun()

