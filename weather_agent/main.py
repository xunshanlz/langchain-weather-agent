from step4_full_agent import weather_agent

if __name__ == '__main__':
    res = weather_agent('北京明天要下雨吗')
    print(res['messages'][-1].content)