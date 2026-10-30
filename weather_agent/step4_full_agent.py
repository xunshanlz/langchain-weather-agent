from langchain_openai import ChatOpenAI
from step3_wrap_tool import weather_tool, dress_advice_tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from config import API_KEY, BASE_URL, TEMPERATURE, MODEL

checkpointer = InMemorySaver()

def weather_agent():
    client = ChatOpenAI(
        api_key=API_KEY,
        base_url=BASE_URL,
        model=MODEL,
        temperature=TEMPERATURE
    )

    agent = create_agent(
        model=client,
        tools=[weather_tool, dress_advice_tool],
        checkpointer=checkpointer,
        system_prompt="你只能查询实时天气，没有未来预报能力。用户问明天/未来天气时，必须明确告知这一点，不得编造。"
    )
    return agent


if __name__ == '__main__':
    agent = weather_agent()
    res = agent.invoke(
        {'messages': [('user', '北京现在多少度')]},
        config={'configurable': {'thread_id': 'demo-1'}}
    )
    print(res['messages'][-1].content)
    res2 = agent.invoke(
        {'messages': [('user', '那适合穿什么')]},
        config={'configurable': {'thread_id': 'demo-1'}}
    )
    print(res2['messages'][-1].content)

