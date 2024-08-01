# Medical Chatbot

Medical Chatbot is a Python-based tool designed to interact with medical documents, retrieve information, and answer questions related to the content of these documents. This project uses various tools and libraries, such as Streamlit, PyPDF2, Hugging Face Transformers, FAISS, and Langchain or LLAMA, to provide a user-friendly interface for querying and extracting information from medical texts.

## Features

1. **PDF/TXT Translation:**
   - Upload PDF or Text documents and translate them into different languages using the Google Translate API.
   - Accessible through a Streamlit GUI for easy interaction.

2. **Question Answering:**
   - Ask questions related to the uploaded medical documents and receive context-based answers.
   - Utilizes Hugging Face Transformers and Langchain for natural language processing and understanding.

3. **Document Vectorization:**
   - Convert PDF/TXT documents into vector representations using Hugging Face embeddings.
   - Store these vectors in a database for efficient retrieval using FAISS.

4. **OCR Integration:**
   - Capture pages from a live camera feed, save them, and perform Optical Character Recognition (OCR) to extract text content.
   - Process the extracted text for further analysis and interaction.

## Workflow

- **`model.py`:** Main file to run the chatbot/QA system. Execute this file to launch the primary functionality of the Medical Chatbot.

- **`ocr.py`:** Contains code to run a live camera feed and perform OCR. This script captures pages, saves them, and extracts text content.

- **`translate.py`:** Responsible for translating input PDFs/TXT files into different languages. Accessible through the Translate Streamlit GUI.

- **`vector_store`:** Folder storing vector representations of PDF and TXT files. These embeddings facilitate efficient document retrieval.

- **`input_pdfs`:** Directory for uploading input PDFs/TXT files. Users can upload medical documents to be processed by the application.

- **`translated_pdfs`:** Directory storing translated PDFs of the input documents. Translation is performed using the Translate Streamlit GUI.

## Installation

To set up the Medical Chatbot locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MapariPrajwal/medical_chatbot.git
   cd medical_chatbot
