from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableSequence

# each runnable has same input and process parallely then produces a dictionary output
load_dotenv()

model = ChatPerplexity(model="sonar")
string_parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a tweet about {topic}",
    input_variables=["topic"],
)
prompt2 = PromptTemplate(
    template="Write a Linkedin post about {topic}",
    input_variables=["topic"],
)
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, string_parser),
    'linkedin' : RunnableSequence(prompt2, model, string_parser)
})
result = parallel_chain.invoke({"topic": "Radio"})
print(result)
print(result['tweet'])