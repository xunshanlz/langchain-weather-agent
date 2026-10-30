from langchain_openai import ChatOpenAI
from config import API_KEY, BASE_URL, TEMPERATURE, MODEL

def create_client():
    client = ChatOpenAI(
        api_key=API_KEY,
        base_url=BASE_URL,
        model=MODEL,
        temperature=TEMPERATURE
    )
    return client


if __name__ == '__main__':
    llm = create_client()
    response = llm.invoke('你好')
    print(response.content)