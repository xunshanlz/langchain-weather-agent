from langchain_openai import ChatOpenAI
from step3_wrap_tool import weather_tool
from langchain.agents import create_agent
from config import API_KEY, BASE_URL, TEMPERATURE, MODEL


def weather_agent(prompt):
    client = ChatOpenAI(
        api_key=API_KEY,
        base_url=BASE_URL,
        model=MODEL,
        temperature=TEMPERATURE
    )

    agent = create_agent(
        model=client,
        tools=[weather_tool],
    )

    response = agent.invoke({'messages': [('user', prompt)]})
    return response
# print(res)

if __name__ == '__main__':
    res = weather_agent('北京明天要下雨吗')
    print(res['messages'][-1].content)
