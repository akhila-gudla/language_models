from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
load_dotenv()

model = ChatPerplexity(model="sonar")

messages=[
    SystemMessage(content="Always answer with only the final result, no explanation, no sources."),
    HumanMessage(content ="Tell me about langchain")
]
result = model.invoke(messages)
messages.append(AIMessage(result.content))
print(messages)