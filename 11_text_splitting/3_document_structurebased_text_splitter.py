#used for code etc
#python splitter 
from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text ="""
print("Hello, World!")
def add_numbers(num1, num2):
  sum_result = num1 + num2
  return sum_result

number1 = 5
number2 = 10
result = add_numbers(number1, number2)
print(f"The sum of {number1} and {number2} is: {result}")
"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0
)
chunks = splitter.split_text(text)
print(chunks[1])