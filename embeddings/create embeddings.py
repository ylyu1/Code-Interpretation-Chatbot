import os
import csv
from docx import Document
import textract
from pinecone import Pinecone
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

# Initialize Pinecone
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone()
index = pc.Index('lightyear')

# Initialize OpenAI Embeddings
embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')

# Initialize Pinecone Vector Store
vectorstore = PineconeVectorStore(index, embeddings)

# Define functions to read different file types
def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_file(file_path):
    _, ext = os.path.splitext(file_path)
    if ext == '.txt':
        return read_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")
    
def rename_files_extention(directory, exts, to_ext):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(exts):
                file_path = os.path.join(dirpath, filename)

                new_filename = filename

                for ext in exts:
                    new_filename = new_filename.replace(ext, to_ext)

                new_filepath = os.path.join(dirpath, new_filename)
                os.rename(file_path, new_filepath)

# Load documents and store embeddings in Pinecone
def load_documents_and_store_embeddings(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(('.txt')):
                file_path = os.path.join(dirpath, filename)
                content = read_file(file_path)
                
                # Generate embedding for the document content
                embedding = embeddings.embed_documents([content])[0]  # chunk_size: None, will use the chunk size specified by the class.
                meta = {'text': content}
                # Store embeddings in Pinecone (or other preferred db) using the filename as the document ID
                index.upsert(vectors=[(filename, embedding, meta)])

src_dir = "C:/Users/ylyu0/Desktop/LLM2024/LightYears/embedding"
rename_files_extention(src_dir, (".h",".cpp"), ".txt")

# Load documents from the specified directory and store their embeddings in Pinecone
load_documents_and_store_embeddings(src_dir)