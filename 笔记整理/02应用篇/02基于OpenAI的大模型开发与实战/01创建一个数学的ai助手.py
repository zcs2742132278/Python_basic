from openai import OpenAI


client = OpenAI(
    api_key="sk-f0d8ae3a2d2e48f1953c4a29ef3a1464",
    base_url="https://api.deepseek.com"  # 改成 DeepSeek 官方地址
)

'''
没有OpenAI的key，舍弃
'''


# 第一步 定义应该assistant
# assistant = client.beta.assistants.create(
#     name='cc',  # 助手名字
#     instructions='你是一个私人数学辅导老师，能够解决数学问题和数学计算。',  # 角色，定位
#     tools=[{'type': 'code_interpreter'}],  # 指定工具
#     model='gpt-5.4'
# )
#
# # 第二步
# thread = client.beta.threads.create()
#
# # 第三步
# message = client.beta.threads.messages.create(
#     thread_id=thread.id,  # 线程id
#     role='主人',
#     content='请帮我解一个方程:4x+10=30'
# )
#
# # 第四步
# # 等待处理完成后，再得到所有结果
# run = client.beta.threads.runs.create_and_poll(
#     thread_id=thread.id,
#     assistant_id=assistant.id,
#     instructions=''
# )
#
# print('run的状态:' + run.status)
#
# if run.status == 'completed':
#     # 输出最终结果
#     messages = client.beta.threads.messages.list(thread_id=thread.id)
#     print('\n消息:\n')
#     for msg in messages:
#         print(f'Role:{msg.role.capitalize()}')  # 大写展示
#         print(msg.content[0].text.value + '\n')
def main_assistant(question):
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[
            {'role': 'user', 'content': question}
        ],
        temperature=0.1,  # 数学问题要严谨
        max_tokens=2000
    )
    return response.choices[0].message.content

question = '  ⎿  API Error: 400 Failed to deserialize the JSON body into the target type: messages[1].role: unknown variant `system`, expected `user` or `assistant` at line 1 column 493'
# 实例
print(main_assistant(f'解决一下{question}，让claude可以正常运行'))