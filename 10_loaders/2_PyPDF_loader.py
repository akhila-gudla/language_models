# only text pdf's , not written or scanned pdf's
#need to install pypdf package
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("/Users/gudlaakhila/Desktop/language_models/10_loaders/computer.pdf")
documents = loader.load()
print(documents[2].page_content)
print(documents[2].metadata)