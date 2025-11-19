from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st

load_dotenv()
model = ChatPerplexity( model="sonar")
st.header('Green code Analyser')
code_input = st.text_area("Enter your Python code here:", height=200, value="print('Hello, Streamlit!')")
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["java", "py","txt"])

template = load_prompt('template.json')

if st.button('Analyse'):
    chain = template | model
    result = chain.invoke({
    'code_input'  : code_input,
#     'style_input'  : style_input,
#     'length_input' : length_input
})
    st.write(result.content)
