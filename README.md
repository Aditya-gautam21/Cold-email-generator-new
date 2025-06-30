# ✉️ Cold Email Generator

An AI-powered **cold email generator** that uses **LangChain**, **Groq Cloud LLM**, **ChromaDB**, and **Streamlit** to automate personalized outreach based on job postings.

---

## 🚀 Features

- **Job Data Extraction**: Scrapes job details from a given URL using `langchain` loaders.
- **Portfolio Matching**: Searches a vector database (ChromaDB) to match skills with portfolio links.
- **Email Generation**: Creates personalized cold emails using a Groq-powered LLM.
- **Streamlit Interface**: User-friendly web app for seamless interaction.

---

## 🧰 Tech Stack

| Component       | Library/Service         |
|----------------|-------------------------|
| Language Model | Groq Cloud (Llama3.1)   |
| Prompt Flow    | LangChain               |
| Vector DB      | ChromaDB                |
| Web UI         | Streamlit               |
| Scraping       | LangChain WebBaseLoader|

---

## ⚙️ Setup

1. **Clone the repo**
    ```bash
    git clone https://github.com/Aditya-gautam21/Cold-email-generator-new.git
    cd Cold-email-generator-new
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Add environment variables**
    - Create a `.env` file in the root:
      ```
      GROQ_API_KEY=your_groq_api_key_here
      ```

---

## 🚩 Usage

To launch the app:
```bash
streamlit run app.py
```

---

## 🗂️ Project Structure

```
.
├── app.py             # Streamlit app entrypoint
├── chain.py           # LangChain flow setup & LLM calls
├── portfolio.py       # Portfolio & vector store logic
├── utils.py           # Helpers (parsing, cleaning, etc.)
├── requirements.txt   # Python dependencies
└── .gitignore
```

---

## 📄 License

MIT License — see `LICENSE` file.

---

## 🤝 Contact

Built by [Aditya Gautam](https://github.com/Aditya-gautam21).