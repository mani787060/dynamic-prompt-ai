# Dynamic Prompt AI Orchestrator
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B)](https://streamlit.io/)
[![LLM](https://img.shields.io/badge/AI-Dynamic%20Prompting-blue)](https://en.wikipedia.org/wiki/Prompt_engineering)

## 🎨 Project Overview
This repository demonstrates a **Dynamic Prompting Interface**, a significant upgrade from static AI tools. Instead of a hardcoded role, this UI allows users to inject custom **System Instructions**, switch between pre-defined personas (e.g., Creative Writer vs. Technical Architect), and see how changing the "Hidden Context" fundamentally alters the AI's behavior.

---

## 🛠️ Technical Features

### 1. Dynamic Context Injection
* **User-Defined Personas:** A dedicated text area to define the AI's character, constraints, and tone in real-time.
* **Template Library:** A sidebar containing pre-set prompt templates for common tasks like "Code Debugging," "Email Drafting," and "SQL Query Generation."

### 2. Multi-Model Steering
* **Provider Agnostic:** Seamlessly toggle between **OpenAI (GPT-4o)**, **Anthropic (Claude)**, and **Google Gemini** using the same dynamic input.
* **Inference Control:** Interactive sliders for `Temperature`, `Top-p`, and `Frequency Penalty` to fine-tune the "creativity" of the dynamic response.

### 3. Session State Management
* **Chat Persistence:** Utilizing `st.session_state` to maintain the conversation flow even when switching between different dynamic prompts.
* **Secure Key Handling:** Built-in support for encrypted API key inputs via the UI or `.env` files.

---

## 💻 Tech Stack
* **Frontend:** Streamlit
* **AI SDKs:** OpenAI, Anthropic, Google Generative AI
* **Language:** Python
* **Environment:** `python-dotenv`

