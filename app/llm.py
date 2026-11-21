from langchain_openai import ChatOpenAI , OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

provider = os.getenv("PROVIDER")
chat_model = os.getenv("CHAT_MODEL")
embedding_model = os.getenv("EMBEDDING_MODEL")
google_key = os.getenv("GOOGLE_API_KEY")
def get_chat_llm():
    if(provider=="Gemini"):
        print(chat_model , type(chat_model) , provider)
        return ChatGoogleGenerativeAI(model=chat_model , api_key=google_key)
    if(provider=="OpenAi"):
        return ChatOpenAI(model=chat_model)


def get_embedding_llm():
    if(provider=="Gemini"):
        return GoogleGenerativeAIEmbeddings(model=embedding_model)
    if(provider=="OpenAi"):
        return OpenAIEmbeddings(model=embedding_model)


def return_response(response):
    print(response)
    if(provider=="Gemini"):
        return response.content[0]['text']
    if(provider=="OpenAi"):
        return response.content