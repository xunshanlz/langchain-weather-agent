from step2_mock_tool import get_weather
from langchain_core.tools import tool

@tool
def weather_tool(city:str) -> dict:
    """查询指定城市的实时天气。city参数是中文城市名，如‘北京’。返回值是一个字典，包含城市名称、天气条件、温度（摄氏度）、湿度（%）和风速（km/h）。
    :param city: 城市名称
    :return: 天气信息
    """
    return get_weather(city)

if __name__ == '__main__':
    print(weather_tool.description)
    print(weather_tool.args)
