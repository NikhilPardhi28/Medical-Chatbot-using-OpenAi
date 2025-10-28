# 🧬 MEDIBOT
**AI-Powered Healthcare Chatbot using OpenAI API**

MediBot is an intelligent healthcare assistant that leverages **OpenAI’s GPT models** to provide reliable, conversational medical information and health guidance.  
It enables users to ask medical or wellness-related questions and receive context-aware, human-like answers — helping bridge the gap between patients and information accessibility.

> ⚠️ **Disclaimer:** MediBot is not a replacement for a licensed healthcare professional. It provides **educational information only** and should not be used for diagnosis or treatment.

---

## 🚀 Project Overview

MediBot acts as a **virtual medical assistant**, using **OpenAI’s GPT-4/5 API** to process user queries in natural language.  
It can explain diseases, symptoms, medications, diet plans, and preventive measures — in a user-friendly, conversational tone.

Optionally, MediBot can be enhanced with:
- **Document upload & retrieval (RAG)** for personalized responses.
- **Speech-to-text & text-to-speech** for accessibility.
- **Multi-language support** for broader reach.

---

## 🧩 Features

✅ Chat with an intelligent medical assistant powered by OpenAI  
✅ Accurate and conversational responses on general health topics  
✅ Optional medical document upload & analysis (PDF/Reports)  
✅ Secure handling of user queries with no data storage  
✅ Built-in safety filters to avoid unsafe or misleading medical advice  
✅ Easy deployment with Streamlit or Flask  

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend / UI | Streamlit |
| Backend | Python |
| AI Model | OpenAI GPT (gpt-4o / gpt-4-turbo / gpt-3.5-turbo) |
| File Handling (optional) | PyMuPDF / pdfplumber |
| Deployment | Streamlit Cloud / Render / Hugging Face Spaces |
| Environment Management | dotenv |

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/medibot.git
cd medibot
2️⃣ Create and activate a virtual environment
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt
Example requirements.txt:

🔑 Environment Variables
Create a .env file in the root directory and add your OpenAI key:

OPENAI_API_KEY=your_openai_api_key_here
If you’re using document retrieval or FAISS:

VECTOR_DB_PATH=./embeddings/index.faiss
▶️ Usage

Run the app
streamlit run app.py
Then open your browser at http://localhost:8501.

Example Interaction
User: “What are the symptoms of anemia?”
MediBot: “Common symptoms include fatigue, pale skin, shortness of breath, and dizziness. However, consult a doctor for proper diagnosis.”

📂 Project Structure
medibot/
│
├── app.py                    # Streamlit app
├── requirements.txt
├── README.md
├── .env.example
│
├── /src
│   ├── chat.py               # OpenAI API interaction
│   ├── ui.py                 # Streamlit UI components
│   ├── pdf_parser.py         # Optional: extract text from PDFs
│   └── utils.py
│
├── /data                     # Optional user uploads
├── /assets                   # Logo / screenshots
└── /embeddings               # FAISS vector store (if using RAG)
🧾 Example Code Snippet


