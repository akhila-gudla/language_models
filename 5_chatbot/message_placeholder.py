from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support assistant.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', ' {query}'),
])

chat_history = []
chat_history_path = '/Users/gudlaakhila/Desktop/language_models/chatbot/chat_history.txt'

with open (chat_history_path) as file:
    chat_history.extend(file.readlines())
print(chat_history)
chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund'})