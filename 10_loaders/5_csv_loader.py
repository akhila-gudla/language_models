from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="/Users/gudlaakhila/Desktop/language_models/10_loaders/Social_Network_Ads.csv",
    encoding="utf-8")
documents = loader.load()
print(documents[0].page_content)