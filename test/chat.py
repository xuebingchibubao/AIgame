from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="Qwen/QwQ-32B",
    url='https://api.siliconflow.cn/v1',
    api_key='sk-qseennfhdprismchczwnkzpohyjmuwgpiaywuclsisgugfvo'
)

agent = ChatAgent(
    model=model,
    output_language='中文'
)

while True:
    str = input("You: ")
    response = agent.step(str)
    print(response.msgs[0].content)