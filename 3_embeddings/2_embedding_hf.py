from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')
#https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
# akhilagudla2101@gmail.com
# Apdkrr1279$
text= "Delhi is capital of india"
vector =embedding.embed_query(text)
print(str(vector))

