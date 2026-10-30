import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("DASHSCOPE_API_KEY")
BASE_URL='https://dashscope.aliyuncs.com/compatible-mode/v1'
TEMPERATURE=0.7
MODEL='qwen-plus'
QWEATHER_API_HOST = os.environ.get("QWEATHER_API_HOST")
QWEATHER_API_KEY = os.environ.get("QWEATHER_API_KEY")




