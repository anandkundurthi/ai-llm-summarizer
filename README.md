#  AI LLM Text Summarizer

An end-to-end AI application that generates concise summaries using Large Language Models (LLMs).
This project demonstrates real-world AI integration using APIs, backend services, and an interactive UI.

---

##  Features

*  AI-powered text summarization
* FastAPI backend for scalable API design
*  Streamlit UI for real-time interaction
*  Fallback mechanism when API fails
*  Modular architecture (API + Logic + UI)
*  Secure API key handling using `.env`

---

##  Architecture

User Input (Streamlit UI)
↓
FastAPI Endpoint (`/summarize`)
↓
LLM Processing (OpenAI API / Mock Fallback)
↓
Response returned to UI

---

##  Tech Stack

* Python
* FastAPI
* OpenAI API (LLM)
* Streamlit
* python-dotenv

---

##  Setup Instructions

```bash
git clone https://github.com/anandkundurthi/ai-llm-summarizer.git
cd ai-llm-summarizer

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

##  Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Run the Application

### Start Backend (FastAPI)

```bash
uvicorn main:app --reload
```

### Start Frontend (Streamlit)

```bash
streamlit run app.py
```

---

##  Demo

*Add your app screenshot here*

```
![App Screenshot](screenshot.png)
```

---

##  Key Learnings

* Integration of LLM APIs into real applications
* Prompt engineering for structured outputs
* API development using FastAPI
* Building interactive UI with Streamlit
* Handling failures using fallback mechanisms

---

##  Future Improvements

*  Add user authentication
*  Deploy on cloud (AWS / Render / Vercel)
*  Add multiple summarization styles
* Add analytics/dashboard

---

##  About This Project

Built as part of hands-on AI/ML engineering practice focusing on real-world LLM integration and production-style architecture.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to connect!
