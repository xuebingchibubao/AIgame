import requests
import shutil

# 生成图像
api_key = "sk-qseennfhdprismchczwnkzpohyjmuwgpiaywuclsisgugfvo"  # 替换为实际API Key

# 修复1: 检查API端点URL是否正确
# 修复2: 添加错误处理
payload = {
    "model": "deepseek-ai/Janus-Pro-7B", 
    "prompt": "星空下的沙漠", 
    "size": "1024x1024"
}
headers = {
    "Authorization": f"Bearer {api_key}", 
    "Content-Type": "application/json"
}

try:
    response = requests.post("https://api.siliconflow.com/v1/images/generations", json=payload, headers=headers)
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {response.text}")
    
    if response.status_code == 200:
        image_url = response.json()["data"][0]["url"]
        
        # 下载图像
        image_response = requests.get(image_url, stream=True)
        with open("desert_stars.png", "wb") as f:
            shutil.copyfileobj(image_response.raw, f)
        print("图片已保存至本地！")
    else:
        print(f"API调用失败: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    print(f"请求错误: {e}")
except KeyError as e:
    print(f"响应格式错误: {e}")