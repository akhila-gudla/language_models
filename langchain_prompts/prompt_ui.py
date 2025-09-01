from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st

load_dotenv()
model = ChatPerplexity( model="sonar")
st.header('Research Tool')
# user_input=st.text_input('Enter your prompt')
paper_input = st.selectbox("Select Research Paper name", ["Select...", "Attention is all you need", "BERT: pre- training of Deep Bidirectional transformers"])
style_input = st.selectbox("Select Explanation Style", ["Beginner","Technical","Code-Oriented","Mathematical"])
length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)","Medium (3-5 paragraphs)", "Long (detailed explanantion)"])

template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
    'paper_input'  : paper_input,
    'style_input'  : style_input,
    'length_input' : length_input
})
    st.write(result.content)
