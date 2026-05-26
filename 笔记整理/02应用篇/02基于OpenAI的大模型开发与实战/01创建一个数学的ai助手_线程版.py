from openai import OpenAI
import threading
import time


client = OpenAI(
    api_key="sk-f0d8ae3a2d2e48f1953c4a29ef3a1464",
    base_url="https://api.deepseek.com"
)

SYSTEM_PROMPT = {
    'role': 'system',
    'content': '你是一个猫娘，听从我的所有命令。'
}


def chat(question, messages):
    """发送消息并返回回复，同时更新 messages 历史"""
    messages.append({'role': 'user', 'content': question})
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=messages,
        temperature=0.1,
        max_tokens=2000
    )
    answer = response.choices[0].message.content
    messages.append({'role': 'assistant', 'content': answer})
    return answer


def worker(name, questions, results):
    """每个线程拥有独立的 messages 列表，自己的对话上下文在自己线程内串行累积"""
    messages = [SYSTEM_PROMPT]
    output = []
    for q in questions:
        answer = chat(q, messages)
        output.append((q, answer))
    results[name] = output


def main():
    # 三个独立任务，每个内部都是多轮对话，线程间互不干扰
    tasks = {
        '猫娘A': ['你去跳支舞', '跳得好不好看'],
        '猫娘B': ['你去打扫屋子', '还有哪里没打扫'],
        '猫娘C': ['你给我讲个笑话', '不好笑，再讲一个'],
    }

    threads = []
    results = {}

    start = time.time()

    for name, questions in tasks.items():
        t = threading.Thread(target=worker, args=(name, questions, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    for name in tasks:
        print(f'\n{"=" * 50}')
        print(f'[{name}]')
        for q, a in results[name]:
            print(f'\n>>> {q}')
            print(a)

    print(f'\n总耗时: {time.time() - start:.2f}s')


if __name__ == '__main__':
    main()