# used for .txt files ( logs, youtube transcripts, etc. )
from langchain_community.document_loaders import TextLoader
from langchain_perplexity import ChatPerplexity
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatPerplexity(model="sonar")
prompt = PromptTemplate(
    input_variables=["poem"],
    template="Please summarize the following poem :\n\n{poem}"
)
parser = StrOutputParser()
loader = TextLoader("/Users/gudlaakhila/Desktop/language_models/10_loaders/cricket.txt", encoding='utf-8')
documents = loader.load()
# print(documents[0])
# print(type(documents[0]))
# print(documents[0].page_content)
# print(documents[0].metadata)

chain = prompt | model | parser 
response = chain.invoke({"poem": documents[0].page_content}) 
print(response)