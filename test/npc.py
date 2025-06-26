from camel.agents import ChatAgent
from camel.configs import ChatGPTConfig
from camel.models import ModelFactory
from camel.types import ModelPlatformType

assistant_model_config = ChatGPTConfig(
    temperature=0.9,
)
model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="Qwen/QwQ-32B",    url='https://api.siliconflow.cn/v1',
    api_key='sk-qseennfhdprismchczwnkzpohyjmuwgpiaywuclsisgugfvo',
    model_config_dict=assistant_model_config.as_dict(),
)

agent = ChatAgent(
    model=model,
    output_language='中文',
)
def interact(str):
    character,info_str=str
    for tup in character:
        name,des=tup
        input=info_str+'你是'+name+'，你的性格如下：'+des+'请以'+name+"为主语写一下接下来的言行，控制在100字以内。要求能够让故事能持续下去，不必完结太快。"
        print(input)
        response = agent.step(input)
        info_str=info_str+response.msgs[0].content
    return(info_str)

#character=[["小明","沉稳内敛，不善言辞，但心思细腻，善于观察细节。做事认真负责，一旦决定的事情就会全力以赴，不达目的绝不罢休。平时话不多，但每句话都经过深思熟虑，给人一种可靠的感觉。"],
#           ["小美","热情开朗，性格外向，善于与人交往，总是能迅速融入新环境。她充满活力，对生活充满热情，喜欢尝试新鲜事物。同时，她也很有同情心，乐于助人，是朋友眼中的“开心果”。"],
#           ["小王","冷静理性，善于分析问题，逻辑思维能力很强。面对复杂的情况，他总能保持冷静，迅速找到解决问题的关键。不过，他有时会显得有些冷漠，对人情世故不太在意，更注重事情的本质和结果。"]]
#info_str="玩家李磊，小明，小美，小王四个人一起玩炸金花，玩家李磊选择作弊。"
#god_data=[character,info_str]
#print(interact(god_data))
