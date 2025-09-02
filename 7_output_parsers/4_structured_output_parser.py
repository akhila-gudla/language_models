from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()
model = ChatPerplexity(model="sonar")

# StructuredOutputParser cant do data validation but it can enforce fixed schema

schema = [
    ResponseSchema(name  = "fact_1", description="fact 1 about topic", type="string"),
    ResponseSchema(name  = "fact_2", description="fact 2 about topic", type="string"),
    ResponseSchema(name  = "fact_3", description="fact 3 about topic", type="string"),
]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template="Give me 3 facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
chain = template | model | parser
result = chain.invoke({'topic':"black hole"})
print(result)