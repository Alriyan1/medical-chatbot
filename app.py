from flask import render_template,Flask,jsonify,request
from src.helper import download_nvidia_embedding
from langchain_pinecone import PineconeVectorStore
from langchain_nvidia import ChatNVIDIA
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os



app = Flask(__name__)


load_dotenv()
os.environ['PINECONE_API_KEY']=os.getenv('PINECONE_KEY')
os.environ['NVIDIA_API_KEY']=os.getenv('NVIDIA_KEY')


embeddings = download_nvidia_embedding()

index_name = 'medical-chatbot'

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding = embeddings
)


retriever = docsearch.as_retriever(search_type = 'similarity',search_kwargs={'k':3})

chatModel = ChatNVIDIA(model='meta/llama-3.3-70b-instruct')

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)


@app.route('/')
def index():
    return render_template('chat.html')


@app.route('/get',methods=['GET','POST'])
def chat():
    msg = request.form['msg']
    input = msg
    print(input)
    response = rag_chain.invoke({'input':msg})
    print('Response : ',response['answer'])
    return str(response['answer'])


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug = True)