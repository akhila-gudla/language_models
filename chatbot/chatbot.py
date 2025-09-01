from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
load_dotenv()
model = ChatPerplexity(model="sonar")

chat_history=[
    SystemMessage(content="Always answer with only the final result, no explanation, no sources.")
]
while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    else:
        result= model.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        print("AI: ",result.content)
print(chat_history)
