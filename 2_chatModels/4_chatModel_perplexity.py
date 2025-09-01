from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv

load_dotenv()
model = ChatPerplexity( model="sonar")
result =model.invoke("what is capital of india")
print(result.content)
