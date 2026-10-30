import zlib

city_weather = {
    "北京": [ {"city": "北京","condition": "晴", "temperature": 10, "humidity": 80, "wind": 5}, {"city": "北京","condition": "多云", "temperature": 15, "humidity": 90, "wind": 4}],
    "上海": [ {"city": "上海","condition": "多云", "temperature": 25, "humidity": 90, "wind": 3}, {"city": "上海","condition": "晴", "temperature": 28, "humidity": 70, "wind": 2}],
    "广州": [ {"city": "广州","condition": "下雨", "temperature": 22, "humidity": 100, "wind": 10}, {"city": "广州","condition": "晴", "temperature": 26, "humidity": 80, "wind": 5}],
    "深圳": [ {"city": "深圳","condition": "晴", "temperature": 28, "humidity": 70, "wind": 4}, {"city": "深圳","condition": "多云", "temperature": 24, "humidity": 90, "wind": 3}],
    "成都": [ {"city": "成都","condition": "多云", "temperature": 20, "humidity": 80, "wind": 2}, {"city": "成都","condition": "晴", "temperature": 26, "humidity": 70, "wind": 4}],
    "哈尔滨": [ {"city": "哈尔滨","condition": "下雪", "temperature": -8, "humidity": 50, "wind": 6}, {"city": "哈尔滨","condition": "晴", "temperature": -2, "humidity": 30, "wind": 3}],
}

def get_weather(city:str) -> dict:
    """
    查询指定城市的实时天气。city参数是中文城市名，如‘北京’。返回值是一个字典，包含城市名称、天气条件、温度（摄氏度）、湿度（%）和风速（km/h）。
    :param city: 城市名称
    :return: 天气信息
    """
    result = city_weather.get(city, [{"city": city, "condition": "多云", "temperature": 20, "humidity": 80, "wind": 2}])
    idx = zlib.crc32(city.encode()) % len(result)
    # todo: 温度用city哈希派生一个数，湿度同上，天气状况从一个通用池里hash挑
    return result[idx]

def dress_advice(temperature:int, condition:str) -> str:
    """
    根据温度和天气条件给出穿衣建议。temperature参数是摄氏度，condition参数是天气条件，如‘晴’、‘多云’、‘下雨’、‘下雪’。返回值是一个字符串，如‘天气晴朗，温度较高，建议穿薄外套。’
    :param temperature: 温度
    :param condition: 天气条件
    :return: 穿衣建议
    """
    temperature_correction = {
        "晴": 0,
        "多云": 0,
        "下雨": -5,
        "下雪": -5
    }
    body_temperature = temperature + temperature_correction.get(condition, 0)
    if body_temperature > 30:
        return "天气晴朗，温度较高，建议穿短袖。"
    elif body_temperature > 20:
        return "天气温和，建议穿长袖衬衫。"
    elif body_temperature > 10:
        return "天气凉爽，建议穿厚外套。"
    else:
        return "天气寒冷，建议穿羽绒服。"


if __name__ == '__main__':
    print(get_weather("北京"))
    print(get_weather("北京"))
    print(get_weather("驻马店"))
    print(get_weather("石家庄"))
