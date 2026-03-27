"""from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI()

st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')



if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)"""


import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# 1. Load your API Key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Setup the Model with the "404 Fix"
# We use gemini-1.5-flash as it's the most reliable for free research tools
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview", 
    google_api_key=api_key,
    temperature=0.3  # Lower temperature for more factual summaries
)

st.header('Research Tool')

# 3. UI Inputs
paper_input = st.selectbox( 
    "Select Research Paper Name", 
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", 
     "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] 
)

style_input = st.selectbox( 
    "Select Explanation Style", 
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] 
) 

length_input = st.selectbox( 
    "Select Explanation Length", 
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] 
)

# 4. Defining the Template (Using a manual template for stability)
template = PromptTemplate.from_template(
    """
    You are a research assistant. Please summarize the research paper: {paper_input}
    
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    
    Provide a clear and insightful response based on these requirements.
    """
)

# 5. The "Summarize" Button Logic
if st.button('Summarize'):
    if api_key:
        with st.spinner("Analyzing research paper..."):
            try:
                # Create the chain
                chain = template | model
                
                # Run the chain
                result = chain.invoke({
                    'paper_input': paper_input,
                    'style_input': style_input,
                    'length_input': length_input
                })

                # --- THE FIX STARTS HERE ---
                # Check if result.content is a list (typical for Gemini 3 Preview)
                if isinstance(result.content, list):
                    # Find the first part that contains text
                    clean_text = ""
                    for part in result.content:
                        if isinstance(part, dict) and 'text' in part:
                            clean_text += part['text']
                    st.write(clean_text)
                else:
                  # If it's already a string, just print it
                  st.write(result.content)
                  # --- THE FIX ENDS HERE ---

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.error("API Key not found. Please check your .env file.")