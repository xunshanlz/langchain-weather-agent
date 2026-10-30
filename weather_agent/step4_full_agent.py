from langchain_openai import ChatOpenAI
from step3_wrap_tool import weather_tool, dress_advice_tool
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
        tools=[weather_tool, dress_advice_tool],
        system_prompt="你只能查询实时天气，没有未来预报能力。用户问明天/未来天气时，必须明确告知这一点，不得编造。"
    )

    response = agent.invoke({'messages': [('user', prompt)]})
    return response
# print(res)

if __name__ == '__main__':
    res = weather_agent('北京明天要出门怎么穿')
    print(res['messages'][-1].content)
