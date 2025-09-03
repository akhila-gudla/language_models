from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnablePassthrough,RunnableSequence

#special type of runnable which just passes the input to output without any change
#used in scenario: 
load_dotenv()
model = ChatPerplexity(model="sonar")
string_parser = StrOutputParser()
prompt1 = PromptTemplate(
    template="Write a joke about {topic}?",
    input_variables=["topic"],
)
prompt2 = PromptTemplate(
    template="Explain the following joke - {text}?",
    input_variables=["text"],
)
joke_gen_chain = RunnableSequence(prompt1, model, string_parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, string_parser),
})
final_chain =RunnableSequence(joke_gen_chain, parallel_chain)
result =final_chain.invoke({"topic": "cricket"})
print(result)
