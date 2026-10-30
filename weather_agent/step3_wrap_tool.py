from step2_mock_tool import get_weather
from step2_mock_tool import dress_advice
from langchain_core.tools import tool


@tool
def weather_tool(city:str) -> dict:
    """查询指定城市的实时天气。city参数是中文城市名，如‘北京’。返回值是一个字典，包含城市名称、天气条件、温度（摄氏度）、湿度（%）和风速（km/h）。
    :param city: 城市名称
    :return: 天气信息
    """
    return get_weather(city)

@tool
def dress_advice_tool(temperature:int, condition:str) -> str:
    """根据温度和天气条件给出穿衣建议。temperature参数是摄氏度，condition参数是天气条件，如‘晴’、‘多云’、‘下雨’、‘下雪’。返回值是一个字符串，如‘天气晴朗，温度较高，建议穿薄外套。’
    :param temperature: 温度，摄氏度
    :param condition: 天气条件，如‘晴’、‘多云’、‘下雨’、‘下雪’
    :return: 穿衣建议
    """
    return dress_advice(temperature, condition)

if __name__ == '__main__':
    print(weather_tool.description)
    print(weather_tool.args)
