from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda,RunnablePassthrough,RunnableSequence,RunnableParallel

def word_count(text: str) -> int:
    """Returns the number of words in the input text."""
    return len(text.split())
# runnable_word_count = RunnableLambda(word_count)

load_dotenv()
model = ChatPerplexity(model="sonar")
string_parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}?",
    input_variables=["topic"],
)
joke_gen_chain = RunnableSequence(prompt1, model, string_parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})
final_chain =RunnableSequence(joke_gen_chain, parallel_chain)

result= final_chain.invoke({'topic':'sky'})
final_result = f"Joke: {result['joke']}\nWord Count: {result['word_count']}"
print(final_result)