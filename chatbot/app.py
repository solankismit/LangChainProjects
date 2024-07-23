from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
    ("system","You are a helpful assistant that translates English to French."),
    ("user","Question:{question}")
]
)

# streamlit framework

st.title("Langchain Demo with OPENAI API")
inpur_text = st.text_input("Search the topic u want")

# OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parsers = StrOutputParser