from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()
model = ChatAnthropic(model='claude-sonnet-4-20250514')
#https://docs.anthropic.com/en/docs/about-claude/models/overview
result= model.invoke("what is capital of India")
print(result.content)