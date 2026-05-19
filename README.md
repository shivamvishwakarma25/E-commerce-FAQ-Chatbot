#  E-commerce FAQ Chatbot

An intelligent customer support chatbot built with **Streamlit**, **Groq (Llama 3.1)**, and the **Bitext customer support dataset**. It answers e-commerce FAQs using a dataset-first retrieval approach, falling back to an LLM when no match is found.

---

##  Features

-  **Conversational Chat UI** — Full chat history with persistent session state
-  **FAQ Retrieval Engine** — Matches user queries against the Bitext customer support dataset before hitting the LLM
-  **LLM Fallback** — Automatically routes unanswered questions to `llama-3.1-8b-instant` via Groq
-  **Quick-Access FAQ Buttons** — One-click buttons for the 6 most common customer questions
-  **Scoped Responses** — System prompt restricts the LLM to customer support topics only
-  **Clean UI** — Developer menu and footer hidden for a polished end-user experience

---

##  Tech Stack

| Technology | Purpose |
|---|---|
| [Python](https://python.org) | Core language |
| [Streamlit](https://streamlit.io) | Web UI framework |
| [Groq](https://groq.com) | LLM inference (Llama 3.1 8B Instant) |
| [Hugging Face Datasets](https://huggingface.co/datasets) | FAQ training data source |
| [Bitext Dataset](https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset) | Customer support Q&A pairs |
| [pandas](https://pandas.pydata.org) | Dataset processing |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

##  Project Structure

```
E-commerce-FAQ-Chatbot/
├── .devcontainer/        # Dev container configuration
├── .streamlit/           # Streamlit configuration
├── app.py                # Streamlit UI & session state management
├── chatbot.py            # Retrieval logic & Groq LLM fallback
├── data_loader.py        # Loads and processes the Bitext FAQ dataset
├── requirements.txt      # Python dependencies
```

---

##  Architecture

```
User Query
    │
    ▼
┌─────────────────────────┐
│  FAQ Retrieval (dataset) │  ──── Match found? ──→  Return dataset answer
└─────────────────────────┘
    │ No match
    ▼
┌─────────────────────────┐
│  Groq LLM Fallback      │  ──→  llama-3.1-8b-instant
│  (customer support only) │
└─────────────────────────┘
```

The chatbot first searches the **Bitext customer support dataset** for a matching query. If no match is found, it falls back to **Groq's Llama 3.1 8B Instant** model, constrained to customer support topics.

---

##  Getting Started

### Prerequisites

- Python 3.8+
- A [Groq](https://console.groq.com) account with an API key
- Internet access (to download the Hugging Face dataset on first run)

### 1. Clone the Repository

```bash
git clone https://github.com/shivamvishwakarma25/E-commerce-FAQ-Chatbot.git
cd E-commerce-FAQ-Chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

>  Get your free API key from [console.groq.com/keys](https://console.groq.com/keys)

### 4. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

##  How to Use

1. Open the app in your browser.
2. Use the **quick-access FAQ buttons** for instant answers to common questions:
   - What's your shipping policy?
   - What payment methods do you accept?
   - What's your delivery time?
   - How do I return an item?
   - How do I track my order?
   - How do I cancel my order?
3. Or type any custom customer support question in the **chat input** at the bottom.
4. The chatbot will respond from the FAQ dataset or the LLM if no match is found.

---

##  Configuration

| Variable | Description | Required |
|---|---|---|
| `GROQ_API_KEY` | Groq API token for LLM fallback | ✅ Yes |

---

##  Key Dependencies

```
streamlit
groq
datasets
pandas
python-dotenv
```

See [`requirements.txt`](./requirements.txt) for the full list.

---

##  Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

##  License

This project is open source. Please check the repository for license details.

---

##  Author

**Shivam Vishwakarma**
- GitHub: [@shivamvishwakarma25](https://github.com/shivamvishwakarma25)

---

>  **Note:** On first run, the app will download the Bitext customer support dataset from Hugging Face (~100MB). Ensure you have a stable internet connection. Subsequent runs will use the cached dataset.
