from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch, RunnableLambda

load_dotenv()
model = ChatPerplexity(model="sonar")
string_parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="sentiment of the feedback, either positive or negative")

pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="classify the following feedback into positive or negative \n {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables= {'format_instructions': pydantic_parser.get_format_instructions()}
)
prompt_positive = PromptTemplate(
    template="Write an appropriate respose to the positive feedback \n {feedback}",
    input_variables=["feedback"],
)
prompt_negative = PromptTemplate(
    template="Write an appropriate respose to the negative feedback \n {feedback}",
    input_variables=["feedback"],
)

classifier_chain = prompt1 | model | pydantic_parser
branch_chain = RunnableBranch(
    # (condition1,chain),
    # (condition2,chain),
    # default chain
    (lambda x: x.sentiment == 'positive', prompt_positive | model | string_parser),
    (lambda x: x.sentiment == 'negative', prompt_negative | model | string_parser),
    RunnableLambda(lambda x: "could not classify feedback")

)
chain = classifier_chain | branch_chain
print(chain.invoke({'feedback': "The food service was bad"}))