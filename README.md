# Medical Chatbot

A web-based medical chatbot application using Flask, LangChain, NVIDIA Embeddings, and Pinecone vector store. The chatbot leverages retrieval-augmented generation (RAG) to answer user queries based on indexed medical documents.

## Features

- Chat interface for user interaction
- Retrieval-augmented generation using LangChain
- NVIDIA embedding model for document representation
- Pinecone vector store for efficient document retrieval
- Responsive UI with Bootstrap

## Project Structure

```
medicalChatbot/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── src/
│   ├── helper.py           # Helper functions for loading and processing documents
│   └── prompt.py           # Prompt templates for the chatbot
├── templates/
│   └── chat.html           # Chatbot UI template
├── static/
│   └── style.css           # Custom styles
├── model.pt                # (Optional) Model file
├── README.md               # Project documentation
└── ...
```

## Setup

1. **Clone the repository**

   ```sh
   git clone <repo-url>
   cd medicalChatbot
   ```

2. **Create and activate a virtual environment**

   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set environment variables**

   Create a `.env` file in the root directory with the following keys:

   ```
   PINECONE_KEY=your-pinecone-api-key
   NVIDIA_KEY=your-nvidia-api-key
   ```

5. **Run the application**

   ```sh
   python app.py
   ```

   The app will be available at [http://localhost:8080](http://localhost:8080).

## Usage

- Open your browser and navigate to `http://localhost:8080`
- Type your medical question in the chat interface and receive answers powered by RAG and LLMs.

## Customization

- To update the prompt or system instructions, edit [`src/prompt.py`](src/prompt.py).
- To change document loading or embedding logic, see [`src/helper.py`](src/helper.py).


---

**Note:** This chatbot is for informational purposes only and should not be used as a substitute