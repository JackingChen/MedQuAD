import re
import requests
import json

# 替换为你的API密钥
API_KEY = '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'
API_URL = 'https://api.openai.com/v1/chat/completions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

def ShrinkPassage(PROMPT,request=['幫我縮短下列文章段落'],content=[]):
    if not PROMPT:
        PROMPT = '\n'.join(request+content)
# 请求数据
    data = {
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': PROMPT}],
        'model': 'gpt-3.5-turbo'  # 指定要使用的模型
    }

    # 发送POST请求
    response = requests.post(API_URL, headers=headers, json=data)

    # 解析返回的数据
    if response.status_code == 200:
        response_data = response.json()
        model_reply = response_data['choices'][0]['message']['content']
        print("Model Reply:", model_reply)
        return model_reply
    else:
        print("Request failed with status code:", response.status_code)
        print("Response:", response.text)
        return False