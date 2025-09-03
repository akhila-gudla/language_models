from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}?",
    input_variables=["topic"],
)
prompt2 = PromptTemplate(
    template="Explain the following joke - {text}?",
    input_variables=["text"],
)
model = ChatPerplexity(model="sonar")
string_parser = StrOutputParser()
chain = RunnableSequence(prompt1, model, string_parser, prompt2, model, string_parser)
print(chain.invoke({"topic": "chickens"}))