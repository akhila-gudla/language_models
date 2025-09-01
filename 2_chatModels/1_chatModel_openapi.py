from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm=ChatOpenAI(model='gpt-4.1-2025-04-14',temperature=0, max_completion_tokens=10)
#https://platform.openai.com/docs/models
result = llm.invoke("what is capital of India")
print(result)
print(result.content)