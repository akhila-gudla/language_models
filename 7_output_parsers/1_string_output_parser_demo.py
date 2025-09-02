from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
model = ChatPerplexity(model="sonar")

template1 = PromptTemplate(
    template="Give me a detailed report on {topic}",
    input_variables=["topic"]
)
template2 = PromptTemplate(
    template="Give me a 5 line summary report on following text {text}",
    input_variables=["text"]
)
prompt1 = template1.invoke({'topic':"AI"})
result = model.invoke(prompt1)
print(result.content)
print("---------------------------------------------------")
prompt2 = template2.invoke({'text':result.content})
result2 = model.invoke(prompt2)
print(result2.content)