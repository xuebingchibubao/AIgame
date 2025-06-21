from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.messages import BaseMessage

from io import BytesIO
import requests
from PIL import Image


model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="Qwen/Qwen2.5-VL-32B-Instruct",
    url='https://api.siliconflow.cn/v1',
    api_key='sk-qseennfhdprismchczwnkzpohyjmuwgpiaywuclsisgugfvo'
)

agent = ChatAgent(
    model=model,
    output_language='中文'
)

# 图片URL
url = "https://img.picui.cn/free/2025/06/21/685615506eb8b.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

user_msg = BaseMessage.make_user_message(
    role_name="User", 
    content="这是一张cv领域论文的abstract，但是有些模糊，请你识别模糊的单词，再还原英文原文，再翻译成中文。", 
    image_list=[img]  # 将图片放入列表中
)

response = agent.step(user_msg)
print(response.msgs[0].content)