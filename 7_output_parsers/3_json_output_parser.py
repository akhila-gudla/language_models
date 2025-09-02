from langchain_perplexity import ChatPerplexity
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# flaw of json parser is its not of fixed schema.we cant enforce it to have fixed schema

load_dotenv()
model = ChatPerplexity(model="sonar")

parser = JsonOutputParser()
template = PromptTemplate(
    template="Give me name, age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
# prompt = template.format()
# result= model.invoke(prompt)
# json_result = parser.parse(result.content)

#updated code with using chain instead of above 3 lines
chain = template | model | parser 

json_result = chain.invoke({})
print(json_result)
print(json_result['name'])