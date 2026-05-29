# ============================================================
# 导入必要的库（库 = 别人写好的工具包，直接拿来用）
# ============================================================

# asyncio：Python 内置的异步编程库，"异步"就是可以一边等网络返回、一边做其他事，不卡住程序
import asyncio
# os：操作系统接口库，用来处理文件路径、目录等操作
import os
# tempfile：临时文件库，用来获取系统临时目录（比如 C:\Users\xxx\AppData\Local\Temp）
import tempfile
# OpenAI：OpenAI 官方的 Python SDK（软件开发工具包），虽然名字叫 OpenAI，但也可以连接其他兼容的 API
from openai import OpenAI

# ============================================================
# 配音生成助手 —— 用大模型生成台词 + edge-tts 合成语音
# 整个流程分两步：
#   步骤1：调用 DeepSeek 大模型，根据你的需求自动写出配音文稿
#   步骤2：调用 edge-tts（微软免费语音服务），把文稿转成 MP3 音频文件
# ============================================================

# ----- 创建 API 客户端 -----
# OpenAI() 会创建一个连接对象，"客户端"就是你和服务器之间的通讯桥梁
client = OpenAI(
    # api_key：你的 API 密钥，相当于"通行证"，用来向服务器证明你有权限使用服务
    # 注意：真实项目中不要把密钥直接写在代码里，应该用环境变量
    api_key="sk-f0d8ae3a2d2e48f1953c4a29ef3a1464",
    # base_url：API 服务器的地址，这里改成了 DeepSeek 的地址（国内可直接访问，无需翻墙）
    # DeepSeek 的 API 和 OpenAI 的接口格式兼容，所以能用同一个 SDK 调用
    base_url="https://api.deepseek.com"
)


def generate_script(prompt, role="你是一个专业配音脚本编剧", style="自然流畅"):
    """使用大模型（DeepSeek）生成配音台词/脚本

    参数说明：
        prompt  : 你的需求描述，比如"写一段广告配音"
        role    : 给大模型设定的角色，决定它用什么语气和视角写脚本
        style   : 配音的风格，如"自然流畅"、"激昂有力"、"温柔舒缓"
    返回值：
        大模型生成的配音文稿文本
    """
    # response：存储服务器返回的完整结果
    # client.chat.completions.create() 相当于给大模型发送一条消息并等待回复
    response = client.chat.completions.create(
        # model：指定要使用的大模型名称，'deepseek-chat' 是 DeepSeek 的通用对话模型
        model='deepseek-chat',
        # messages：发送给大模型的消息列表，每条消息包含 role（角色）和 content（内容）
        # 至少要有一条 system 消息（给模型设定身份）和一条 user 消息（你的问题）
        messages=[
            # system 消息：定义 AI 的角色和行为规范，类似"你是一个XX，请按XX方式回答"
            # 这段消息告诉模型它是配音编剧，以及输出的格式要求
            # user 消息：你具体想要什么
            {'role': 'user', 'content': prompt}
        ],
        # temperature：控制输出的"创造性"程度，范围 0~2
        # 0.1 很严谨（适合数学），0.7 较有创意（适合写脚本），1.0+ 天马行空
        temperature=0.7,
        # max_tokens：限制回复的最大长度（中文大约 1 个字 = 1~1.5 tokens）
        max_tokens=3000
    )
    # response 是一个嵌套对象，真正的回复文本藏在 choices[0].message.content 里
    # choices[0]：服务器返回的第 1 个候选回复（一般只有 1 个）
    # .message.content：提取回复的文本内容
    return response.choices[0].message.content


async def text_to_speech(text, voice="zh-CN-XiaoxiaoNeural", output_path=None, rate="+0%"):
    """使用微软 Edge 免费 TTS 服务将文本转成语音（MP3 文件）

    async 关键字说明：
        async def 定义的是一个"异步函数"，调用时不会立即执行，返回一个 coroutine 对象。
        异步 = 不阻塞主线程，等待网络IO时可以让出控制权做别的事。

    TTS 是什么？
        TTS = Text-To-Speech（文本转语音），把文字变成真人般的朗读音频。
        edge-tts 使用的是微软 Edge 浏览器内置的免费语音合成引擎，无需付费。

    参数说明：
        text        : 要转换成语音的文本内容
        voice       : 配音角色（说话人的音色），默认用 Xiaoxiao（活泼女声）
        output_path : MP3 文件保存路径，不传则保存到系统临时目录
        rate        : 语速控制，'+0%' 表示正常速度，'+20%' 加速 20%，'-20%' 减速 20%

    返回值：
        MP3 文件的保存路径

    ----- 可选中文配音角色总览 -----

    女声（共 10 种）：
      zh-CN-XiaoxiaoNeural    活泼女声（默认）- 适合日常/娱乐配音
      zh-CN-XiaoyiNeural      温柔女声      - 适合情感类内容
      zh-CN-XiaochenNeural    冷静女声      - 适合科技/知识类内容
      zh-CN-XiaohanNeural     温柔女声      - 细腻柔和
      zh-CN-XiaomengNeural    可爱女声      - 适合儿童/萌系内容
      zh-CN-XiaomoNeural      知性女声      - 适合文艺/叙事内容
      zh-CN-XiaoqiuNeural     温婉女声      - 适合情感故事
      zh-CN-XiaoshuangNeural  爽朗女声      - 适合促销/户外内容
      zh-CN-XiaoxuanNeural    优雅女声      - 适合高端品牌/奢侈品
      zh-CN-XiaoruiNeural     理性女声      - 适合财经/科技解说

    男声（共 3 种）：
      zh-CN-YunxiNeural       青年男声      - 适合日常/青春类内容
      zh-CN-YunjianNeural     成熟男声      - 适合纪录片/权威解说
      zh-CN-YunyangNeural     新闻男声      - 适合新闻播报/正式场合
    """
    # 把 import 放在函数里（懒加载），好处是：
    # 如果用户只用 generate_script 而不调用 TTS，就不会报缺少 edge_tts 的错误
    import edge_tts  # edge-tts 是第三方库，需要 pip install edge-tts 安装

    # ----- 决定输出路径 -----
    # 如果调用者没有传 output_path，就默认存到系统临时目录
    if output_path is None:
        # tempfile.gettempdir() 获取系统临时目录
        # Windows: C:\Users\你的用户名\AppData\Local\Temp
        # 用 os.path.join 拼接路径，比直接用 + '/' 更安全，会自动处理不同系统的路径分隔符
        output_path = os.path.join('E:\code\pycharm\笔记整理\\02应用篇\\02基于OpenAI的大模型开发与实战', "dubbing_output.mp3")

    # ----- 调用 TTS -----
    # edge_tts.Communicate() 创建 TTS 通信对象
    # 参数：
    #   text  : 要转换的文本
    #   voice : 音色角色
    #   rate  : 语速，'+0%' 正常，'+50%' 1.5倍速，'-30%' 0.7倍速
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    # communicate.save(path) 会连接微软服务器，下载合成后的音频，保存到本地
    # await 关键字：等这个异步操作完成再继续往下执行（网络请求需要时间，但不阻塞其他异步任务）
    await communicate.save(output_path)
    # 返回最终保存的文件路径，方便调用者知道文件在哪儿
    return output_path


async def generate_dubbing(prompt, voice="zh-CN-XiaoxiaoNeural", output_dir=None):
    """一键配音：先让大模型写脚本，再把脚本转成语音

    这是整个脚本的核心入口函数，串联起了"写脚本"和"配音"两大步骤。

    参数说明：
        prompt     : 你想要什么内容的配音，用自然语言描述即可
        voice      : 配音角色名称（默认活泼女声）
        output_dir : 音频输出目录，不传则保存到本脚本所在的目录

    返回值：
        (脚本文本, MP3音频文件路径) —— 一个元组
    """
    # ----- 步骤 1/3：生成脚本 -----
    # '=' * 50 会在控制台输出 50 个等号，用作分隔线，让输出看起来更清晰
    print("=" * 50)
    print("[1/3] 正在用大模型生成配音脚本...")
    # 直接调用之前定义的 generate_script 函数（注意：这里没有 await，因为它是普通函数）
    script = generate_script(prompt)
    # f-string（f""）：Python 的字符串格式化方式，花括号 {} 里的变量会被替换成实际值
    # len(script) 返回字符串的字符数
    print(f"脚本生成完成 ({len(script)} 字符):\n{script}\n")

    # ----- 步骤 2/3：合成语音 -----
    print("[2/3] 正在合成语音...")
    # 如果没有指定输出目录，默认存到本脚本所在的目录
    if output_dir is None:
        # __file__ ：当前脚本的完整路径
        # os.path.abspath(__file__) ：转成绝对路径（比如 '.\script.py' → 'E:\code\...\script.py'）
        # os.path.dirname() ：取路径中的目录部分（去掉文件名）
        output_dir = os.path.dirname(os.path.abspath(__file__))
    # 拼接最终输出路径：目录 + 文件名
    output_path = os.path.join(output_dir, "配音输出.mp3")
    # 调用 TTS 函数，传入脚本内容和配音角色
    # await：等语音合成完再继续（合成需要联网下载，可能几秒到几十秒）
    await text_to_speech(script, voice, output_path)

    # ----- 步骤 3/3：完成 -----
    print(f"[3/3] 配音已保存到: {output_path}")
    # 返回脚本和文件路径，方便你后续可能还想拿这些信息做别的事
    return script, output_path


# ============================================================
# 程序入口点 —— 以下代码只在"直接运行此脚本"时执行
# ============================================================

# if __name__ == '__main__': 是 Python 的约定俗成写法
#   如果直接运行本文件（python 02配音生成助手.py），__name__ 的值就是 '__main__'
#   如果本文件被其他脚本 import 导入，__name__ 的值就是模块名 '02配音生成助手'，不会执行这里
# 这样做的好处：这个脚本既能单独运行，也能被其他脚本导入复用，互不影响
if __name__ == '__main__':
    # ----- 定义你的配音需求 -----
    # 这里用自然语言描述你想要什么，大模型会根据这个描述自动写出配音文稿
    prompt = "用猫娘的语气和我说一段10秒的语音"

    # ----- 运行 -----
    # asyncio.run() 是 Python 3.7+ 的标准用法，用于启动并执行一个异步函数
    # generate_dubbing 是一个 async 函数，不能直接调用，必须用 asyncio.run() 包裹
    asyncio.run(generate_dubbing(prompt))