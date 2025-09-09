from langchain_community.document_loaders import WebBaseLoader
from bs4 import BeautifulSoup
# works better with static web pages
loader = WebBaseLoader("https://www.soundcityreading.net/level-1---learning-the-alphabet-pdfs.html")
documents = loader.load()
print(documents[0].page_content)