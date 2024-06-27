import os
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

pinecone_api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone()

index_name = 'lightyear'
index = pc.Index(index_name)
index.describe_index_stats()

llm = ChatOpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

text_field = "text"
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
vectorstore = PineconeVectorStore(index, embeddings, text_field)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

query = "How to change the damage of a bullet?"
query = "how to set the window size when creating an application"
query = "how memory is managed in the game engine"
query = "how to change the key binding for player spaceship movement"
query = "where is the entry point of this program, and which file contains it?"
query = "how to control the frame rate of the game?"
result = qa.invoke(query)
print(result["result"])