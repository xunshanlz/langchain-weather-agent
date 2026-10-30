import requests

from config import QWEATHER_API_HOST, QWEATHER_API_KEY


def get_location_id(city:str) -> str:
    """
    根据城市名称获取城市ID。
    :param city: 城市名称
    :return: 城市ID
    """
    try:
        resp = requests.get(
            url=f'{QWEATHER_API_HOST}/geo/v2/city/lookup',
            params={'location': city, 'key': QWEATHER_API_KEY, 'lang': 'zh'},
            timeout=10
        )
    except  requests.exceptions.RequestException:
        return '天气服务暂时不可用'

    if resp.status_code == 200 and resp.json()['location']:
        city_id = resp.json()['location'][0]['id']
        return city_id
    else:
        return None

def get_real_weather(city:str) -> dict:
    """
    获取指定城市的实时天气。
    :param city: 城市名称
    :return: 实时天气信息，包含城市名称、天气条件(晴、多云等)、温度（摄氏度）、湿度和风速（km/h）
    """
    city_id = get_location_id(city)
    if not city_id:
        return '无法获取城市ID'
    try:
        resp = requests.get(
            url=f'{QWEATHER_API_HOST}/v7/weather/now',
            params={'location': city_id, 'key': QWEATHER_API_KEY, 'lang': 'zh'},
            timeout=10
        )
    except  requests.exceptions.RequestException:
        return '天气服务暂时不可用'

    response = resp.json()
    weather_information={
        'city': city,
        'condition': response['now']['text'],
        'temperature': int(response['now']['temp']),
        'humidity': int(response['now']['humidity']),
        'wind': int(response['now']['windSpeed']),
    }
    return weather_information

if __name__ == '__main__':
    print(get_real_weather('北京'))
    print(get_real_weather('驻马店'))
    print(get_real_weather('哈哈市'))