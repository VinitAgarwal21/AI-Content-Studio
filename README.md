# 🚀 AI Content Studio

Generate high-quality, human-like posts for **LinkedIn, Instagram, and X (Twitter)** using LLMs, prompt engineering, and modular AI pipelines.

---

## ✨ Features

* 🎯 **Multi-platform content generation**

  * LinkedIn → professional, insightful posts
  * Instagram → engaging, storytelling captions
  * X (Twitter) → short, witty content

* 🧠 **Prompt-engineered outputs**

  * Avoids generic AI tone
  * Produces natural, human-like writing

* ⚙️ **Modular architecture**

  * UI (Streamlit)
  * Prompt Builder
  * Generator
  * Output Parser
  * Formatter & Validator

* 📦 **Structured LLM outputs (JSON parsing)**

* 🎛️ Customizable inputs:

  * Tone
  * Audience
  * Key points
  * Call-to-action

---

## 🏗️ Project Structure

```
.
├── app.py
├── components/
│   ├── linkedin_ui.py
│   ├── instagram_ui.py
│   ├── twitter_ui.py
│
├── core/
│   ├── prompt_builder.py
│   ├── generator.py
│   ├── parser.py
│   ├── formatter.py
│   ├── validator.py
│
├── llm/
│   └── llm_helper.py
│
├── models/
│   └── schemas.py
│
└── data/
```

---

## ⚡ How It Works

```text
User Input (UI)
   ↓
Structured Data (dict)
   ↓
PromptTemplate (LangChain)
   ↓
LLM (Generation)
   ↓
JSON Output Parser
   ↓
Formatter + Validator
   ↓
Final Post
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Content-Studio.git
cd AI-Content-Studio
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🧠 Tech Stack

* **Python**
* **Streamlit** (UI)
* **LangChain** (Prompt + LLM pipeline)
* **OpenAI / LLM APIs**
* **Pydantic** (optional structured outputs)

---

## 🔥 Key Learnings

This project demonstrates:

* ✅ Prompt Engineering
* ✅ Structured LLM Outputs (JSON parsing)
* ✅ Modular AI system design
* ✅ Multi-platform content adaptation
* ✅ Building production-style GenAI apps

---

## 🚀 Future Improvements

* 🔁 Regenerate / refine posts
* 📊 Post quality scoring
* 🧠 Multi-step agent pipeline (hook → body → hashtags)
* 💾 Save & manage generated posts
* 🌐 Deploy as SaaS

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork, improve, and submit a PR 🚀

---

## 📌 Author

**Vinit Agarwal**
B.Tech ECE @ IIIT Una
ML | GenAI | Full Stack

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!
