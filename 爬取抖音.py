import requests
import re

# 抖音分享链接（用复制的 v.douyin.com 短链接，别用长链接）
douyin_url = "https://v.douyin.com/-PlcxyCJKrI/"

def get_douyin_info(url):
    # 更完整的 headers，模拟真实浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.douyin.com/"
    }

    # 发起请求，跟随重定向
    try:
        response = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        html = response.text
    except Exception as e:
        print("请求失败：", e)
        return

    # 修正正则，匹配带转义引号的字段
    try:
        # 标题
        title = re.findall(r'"desc":"(.*?)"', html, re.S)[0]
        # 视频ID
        vid = re.findall(r'"aweme_id":"(.*?)"', html)[0]
        # 封面图
        cover = re.findall(r'"cover":"(.*?)"', html)[0]
        # 作者名字
        nickname = re.findall(r'"nickname":"(.*?)"', html)[0]

        print("===== 抖音视频信息 =====")
        print("视频ID：", vid)
        print("标题：", title)
        print("作者：", nickname)
        print("封面：", cover)

    except IndexError:
        print("获取失败，链接可能无效或已过期，也可能是正则没匹配到")
        # 调试：把部分html打印出来，看看有没有目标字段
        print("\n--- 页面片段（用于调试）---")
        print(html[:1000])

# 运行
get_douyin_info(douyin_url)