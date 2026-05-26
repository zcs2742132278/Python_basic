import os

# 代理（如果你国内访问需要，不需要就删掉这两行）
# os.environ['http_proxy'] = '127.0.0.1:7890'
# os.environ['https_proxy'] = '127.0.0.1:7890'

# 重点：用 OpenAI SDK 连接 DeepSeek 平台
from openai import OpenAI

client = OpenAI(
    api_key="sk-f0d8ae3a2d2e48f1953c4a29ef3a1464",
    base_url="https://api.deepseek.com"  # 改成 DeepSeek 官方地址
)
# 调用 DeepSeek 示例
# deepseek的模型常用的有两种     deepseek-reasoner  +  deepseek-chat
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "你的模型有哪几种？"}
    ],
    temperature=0.1,        # 严谨度，越低越准确 ,随机性，创造力，多样性 0.0最严谨 0.7平衡 1.0放飞
    # top_p=0.9,              # 控制词汇多样性，一般不用改，和temperature 二选一即可
    # stop=['\n','结束'],      #遇到什么字符就停止生成
    # n=2,                #生成2个结果           deepseek不支持返回多个结果
    max_tokens=2000,        # 最大字数
    stream=False,           # 是否流式输出
    frequency_penalty=0.2   # 减少重复
)
# print("===正在获取可用模型列表===")
# models = client.models.list()   #通用方法
#
# for idx,model in enumerate(models.data,1):
#     print(f'{idx},{model,id}')
# deepseek-v4-flash  deepseek-v4-pro

# print('=====')
#
# for i in models:
#     print(i)
#
# print('=====')
#
# print(models)

# for i, choice in enumerate(response.choices):
#     print(f"【回答 {i+1}】")
#     print(choice.message.content)
#     print()
print(response.choices[0].message.content)
# print(response.choices[1].message.content)