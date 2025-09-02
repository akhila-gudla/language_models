from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from langchain.output_parsers import PydanticOutputParser


# can do data validation & constraints with pydantic output parser and also enforce fixed schema
load_dotenv()
model = ChatPerplexity(model="sonar")

class Person(BaseModel):
    name: str = Field(description="name of person")
    age: int = Field(gt=18, description= "age of person, must be greater than 18")
    city: str = Field(description="Name of the city the person belongs to")
    profession: str = Field(description="profession of the person")

parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(
    template="Generate  name, age and city of a fictional {place} person \n {format_instructions}",
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)
chain = template | model | parser
result = chain.invoke({'place':"American"})
print(result)