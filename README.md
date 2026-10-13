
# 🎨 Dynamic Prompt AI Orchestrator

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit)
![Generative AI](https://img.shields.io/badge/Field-Generative%20AI-green)
![Prompt Engineering](https://img.shields.io/badge/Concept-Prompt%20Engineering-purple)

## 📌 Project Overview

**Dynamic Prompt AI Orchestrator** is a Python-based Generative AI application designed to explore how customized instructions influence the responses produced by large language models (LLMs).

Built with Streamlit, the application provides an interactive interface for configuring system instructions, selecting predefined prompt personas, and experimenting with different prompting strategies.

Instead of relying on one fixed instruction, dynamic prompting allows users to modify the context, tone, and behavior expected from an AI model. The project demonstrates how prompt engineering and model configuration can be combined in a single interface.

## 🎯 Project Objectives

- Understand the role of system instructions in LLM applications.
- Experiment with user-defined personas and prompt templates.
- Explore how different instructions influence model responses.
- Integrate multiple LLM providers through a unified interface.
- Manage conversation state using Streamlit.
- Practice API credential management and basic error handling.

## ⚙️ Key Features

### 1. Dynamic Prompt Engineering

Customize the instructions sent to the language model at runtime.

- Define the model's role, tone, and constraints.
- Switch between predefined personas, such as a creative writer or technical architect.
- Explore how changing instructions affects generated responses.

### 2. Reusable Prompt Templates

Use predefined templates for common tasks, including:

- Code debugging
- Email drafting
- SQL query generation

Templates provide a starting point for common tasks and can reduce the need to rewrite similar instructions repeatedly.

### 3. Multi-Provider LLM Integration

The project is designed to work with supported language model providers, including:

- OpenAI
- Anthropic Claude
- Google Gemini

A unified prompting workflow makes it easier to explore how different models respond to similar instructions. Availability depends on the provider configuration, API credentials, and supported models.

### 4. Generation Parameter Controls

Experiment with generation parameters to understand their influence on model output.

- **Temperature:** Controls the randomness of token selection.
- **Top-p:** Limits token selection to a probability-based group of candidate tokens.
- **Frequency penalty:** Can discourage repeated tokens or phrases in supported APIs.

The exact behavior and supported parameter ranges depend on the selected provider and model.

### 5. Conversation State Management

Streamlit's `st.session_state` can maintain conversation-related information across application reruns.

This helps preserve the interaction flow while users experiment with prompts. Conversation persistence across browser sessions or application restarts would require additional storage.

### 6. API Key Configuration

The application supports API credentials supplied through the interface or environment configuration, as described in the project setup.

Using environment variables or a `.env` file helps keep credentials separate from source code. API keys should never be committed to a public repository.

## 🧠 How It Works

The application follows this general workflow:

1. **Configure the prompt:** Enter custom system instructions or select a predefined template.
2. **Choose the model provider:** Select an available LLM provider and configured model.
3. **Adjust generation settings:** Configure supported parameters such as temperature and top-p.
4. **Submit the request:** Send the prompt and relevant conversation context to the selected model.
5. **Generate the response:** Receive the model's generated text.
6. **Display the output:** Present the response through the Streamlit interface.
7. **Maintain context:** Preserve relevant conversation state during the session.

## 🛠️ Technology Stack

- **Programming Language:** Python
- **Web Interface:** Streamlit
- **LLM Providers:** OpenAI, Anthropic, Google Gemini
- **Configuration:** python-dotenv
- **State Management:** Streamlit Session State

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- API credentials for the provider or providers you want to use
- Internet access for hosted model APIs

### 1. Clone the Repository

```bash
git clone https://github.com/mani787060/dynamic-prompt-ai.git
cd dynamic-prompt-ai
```

### 2. Install Dependencies

Install the packages required by your Python implementation. A possible starting point is:

```bash
pip install streamlit python-dotenv openai anthropic google-generativeai
```

Check the imports in your `.py` file and install any additional dependencies it requires. SDK versions and provider APIs may change over time.

### 3. Configure API Credentials

Create a `.env` file in the project directory and add the credentials for the providers you intend to use.

```env
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
```

Replace the placeholders with your actual credentials. Configure only the providers you use.

Add `.env` to `.gitignore` to prevent accidental publication of API keys.

### 4. Run the Application

```bash
streamlit run your_script.py
```

Replace `your_script.py` with the actual Python filename in your repository.

### 5. Experiment With Prompts

1. Open the local URL displayed by Streamlit.
2. Choose a prompt template or enter custom system instructions.
3. Select an available model provider.
4. Adjust supported generation parameters.
5. Submit a prompt and compare the resulting responses.

## 🌍 Potential Applications

- AI writing and content generation
- Programming assistance and code explanation
- SQL query assistance
- Technical question answering
- Prompt engineering experiments
- Prototyping LLM-powered applications

These are potential applications of the techniques demonstrated by the project, rather than claims that each is a separate implemented feature.

## 📚 Key Learning Outcomes

This project provides practical exposure to:

- System prompts and dynamic context injection
- Prompt templates and persona-based prompting
- LLM API integration
- Generation parameters and model behavior
- Session state in Streamlit
- Environment-based configuration
- Multi-provider application design

## 🔮 Future Improvements

- Add side-by-side comparison of responses from multiple models.
- Support reusable, user-saved prompt templates.
- Add conversation export and import.
- Introduce structured output formats such as JSON.
- Add tool calling and function calling.
- Integrate retrieval-augmented generation (RAG).
- Add prompt evaluation and response-quality metrics.
- Improve validation, logging, and provider-specific error handling.
- Support secure deployment with managed secrets.

## ⚠️ Important Notes

- Model access and API pricing depend on the selected provider.
- Generated responses may contain incorrect or misleading information.
- Different providers may support different generation parameters.
- API credentials must be kept private.
- Verify that the configured SDKs and model names are compatible with the current provider APIs.

## ✅ Conclusion

Dynamic Prompt AI Orchestrator demonstrates how customizable instructions, reusable prompt templates, and LLM API integrations can be combined in an interactive Python application.

The project provides a foundation for understanding prompt engineering and developing more advanced Generative AI applications, including multi-model systems, structured generation, and RAG-based workflows.
