from step4_full_agent import weather_agent


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