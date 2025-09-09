from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path ="/Users/gudlaakhila/Desktop/language_models/10_loaders/books",
    glob="**/*.pdf",
    loader_cls=PyPDFLoader)
documents = loader.load()
print(len(documents))
print(documents[2].page_content)