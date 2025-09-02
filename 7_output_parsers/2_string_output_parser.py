from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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
parser = StrOutputParser()
chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':"black hole"})
print(result)