import requests
import re

# -------------------------- 这里换成你自己的视频短链接 --------------------------
# 必须用抖音App里「分享」→「复制链接」拿到的 https://v.douyin.com/xxx/ 格式
douyin_url = ""

def get_douyin_info(url):
    # 更真实的浏览器请求头，降低被拦截概率
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Referer": "https://www.douyin.com/",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    }

    # 发起请求，跟随重定向，设置超时
    try:
        print("正在请求视频页面...")
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=True,
            timeout=15
        )
        response.raise_for_status()  # 检查请求是否成功（404/500会报错）
        html = response.text
        print(f"请求成功，页面长度：{len(html)} 字符")
    except Exception as e:
        print(f"请求失败：{e}")
        return

    # 适配抖音新页面结构的正则（带容错，没匹配到也不会崩溃）
    try:
        # 视频标题/描述
        title_pattern = re.compile(r'"desc":"(.*?)"', re.S)
        title_match = title_pattern.findall(html)
        title = title_match[0] if title_match else "未获取到标题"

        # 视频ID
        vid_pattern = re.compile(r'"aweme_id":"(.*?)"')
        vid_match = vid_pattern.findall(html)
        vid = vid_match[0] if vid_match else "未获取到视频ID"

        # 作者昵称
        nickname_pattern = re.compile(r'"nickname":"(.*?)"')
        nickname_match = nickname_pattern.findall(html)
        nickname = nickname_match[0] if nickname_match else "未获取到作者名"

        # 封面图链接
        cover_pattern = re.compile(r'"cover_url":"(.*?)"')
        cover_match = cover_pattern.findall(html)
        cover = cover_match[0] if cover_match else "未获取到封面链接"

        # 打印结果
        print("\n===== 抖音视频信息 =====")
        print(f"视频ID：{vid}")
        print(f"作者：{nickname}")
        print(f"标题/描述：{title}")
        print(f"封面链接：{cover}")

    except Exception as e:
        print(f"解析页面失败：{e}")
        print("\n--- 调试用：前2000字符页面片段 ---")
        print(html[:2000])

# 运行
if __name__ == "__main__":
    get_douyin_info(douyin_url)