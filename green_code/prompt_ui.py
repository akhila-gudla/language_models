from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import streamlit as st
import re
import pandas as pd

load_dotenv()
model = ChatPerplexity(model="sonar")
st.header('Green code Analyser')
code_input = st.text_area("Enter your code here:", height=200)
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["java", "py","txt"])

pattern = r"Original_Energy_Used:\s*([\d.]+)\s*\w*\s*" \
          r"Original_CO2_Emitted:\s*([\d.]+)\s*\w*\s*" \
          r"Optimized_Energy_Used:\s*([\d.]+)\s*\w*\s*" \
          r"Optimized_CO2_Emitted:\s*([\d.]+)\s*\w*\s*" \
          r"CO2_Reduction_Percent:\s*([\d.]+)%"

template = load_prompt('template.json')
file_content = ""
if uploaded_file is not None:
    try:
        file_content = uploaded_file.read().decode("utf-8")
    except UnicodeDecodeError:
        file_content = uploaded_file.read().decode("latin-1")  # fallback decoding

if st.button('Analyse'):
    chain = template | model
    result = chain.invoke({
        'code_input': file_content,
    })

    st.write(result.content)

    # Perform regex only after result exists
    match = re.search(pattern, result.content, re.MULTILINE)

    if match:
        orig_energy = float(match.group(1))
        orig_co2 = float(match.group(2))
        opt_energy = float(match.group(3))
        opt_co2 = float(match.group(4))
        reduction_percent = match.group(5)

        col1, col2, col3 = st.columns(3)

        col1.metric("Original Energy Used", f"{orig_energy} units")
        col2.metric("Optimized Energy Used", f"{opt_energy} units",
                    f"{orig_energy - opt_energy} saved")
        col3.metric("CO₂ Reduction", reduction_percent)
        st.divider()
    else:
        st.warning("⚠ Could not extract metrics from model output.")
