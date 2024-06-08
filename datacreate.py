# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter

# DATA_PATH = 'data/'
# DB_FAISS_PATH = 'vectorstore/db_faiss'

# def create_vector_db():
#     loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
#     documents = loader.load()
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     texts = text_splitter.split_documents(documents)
#     embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
#     db = FAISS.from_documents(texts, embeddings)
#     db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
#     db.save_local(DB_FAISS_PATH)

# if __name__ == "__main__":
#     create_vector_db()




from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

DATA_PATH = 'data/'
DB_FAISS_PATH = 'vectorstore/db_faiss'

def create_vector_db():
    loader = DirectoryLoader(DATA_PATH, glob='*.pdf', loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    db = FAISS.from_documents(texts, embeddings)
    db.save_local(DB_FAISS_PATH)

if __name__ == "__main__":
    os.makedirs(DB_FAISS_PATH, exist_ok=True)
    create_vector_db()
