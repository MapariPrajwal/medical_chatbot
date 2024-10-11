from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader,PyPDFLoader

DATA_PATH = 'input_pdfs/disease_treatment_guidelines.pdf'
DB_FAISS_PATH = 'vectorstore/db_faiss'

def create_vector_db():

  loader = PyPDFLoader(DATA_PATH)

  try:
    documents = loader.load()
  except FileNotFoundError:
    print("Could not access input pdfs folder")

  #documents = loader.load()

  print("Documents loaded")

<<<<<<< HEAD
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
=======
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
>>>>>>> 550dd530a87defcd66c3fb2694b765db6210e87c

  texts = text_splitter.split_documents(documents)

  embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})

  db = FAISS.from_documents(texts, embeddings)

  db.save_local(DB_FAISS_PATH)

  print("Vector DB created")

if __name__ == "__main__":
   create_vector_db()