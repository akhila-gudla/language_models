from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')
#https://ai.google.dev/gemini-api/docs/models
result = model.invoke("what is capital of India")
print(result.content)
