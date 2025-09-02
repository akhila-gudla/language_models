from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv

load_dotenv()
# https://docs.perplexity.ai/getting-started/models
model = ChatPerplexity( model="sonar")
result =model.invoke("what is capital of india")
print(result.content)
