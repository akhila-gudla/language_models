# simply based on length it will chunk the text
# https://chunkviz.up.railway.app/
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
text = """These missions have not only expanded our knowledge of the universe but have also
contributed to advancements in technology here on Earth. Satellite communications, GPS, and
even certain medical imaging techniques trace their roots back to innovations driven by
space programs."""

loader = PyPDFLoader("/Users/gudlaakhila/Desktop/language_models/10_loaders/computer.pdf")
documents = loader.load()

splitter = CharacterTextSplitter(
    separator='', 
    chunk_size=100, 
    chunk_overlap=0)
chunks = splitter.split_documents(documents)
print(chunks[0].page_content)
