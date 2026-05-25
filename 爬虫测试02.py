from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import re

# -------------------------- 换成你自己的视频短链接 --------------------------
# douyin_url = "https://v.douyin.com/-PlcxyCJKrI/"
douyin_url = ""

def get_douyin_info(url):
    # 配置 Chrome 浏览器，模拟真实用户
    options = webdriver.ChromeOptions()
    # 取消无头模式，方便你看浏览器操作过程
    # options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")

    # 启动浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    try:
        print("正在打开视频页面...")
        driver.get(url)
        # 等待页面加载（抖音加载需要一点时间）
        time.sleep(5)

        # 获取页面完整HTML
        html = driver.page_source
        print(f"页面加载完成，长度：{len(html)} 字符")

        # 查找包含视频数据的 script 标签
        pattern = re.compile(r'<script id="RENDER_DATA" type="application/json">(.*?)</script>', re.S)
        match = pattern.findall(html)

        if not match:
            print("未找到RENDER_DATA标签，打印前3000字符调试：")
            print(html[:3000])
            return

        # 解析JSON数据
        render_data = json.loads(match[0])
        video_info = render_data.get("aweme", {}).get("detail", {})

        print("\n===== 抖音视频信息 =====")
        print("视频ID：", video_info.get("aweme_id", "未获取到"))
        print("作者：", video_info.get("author", {}).get("nickname", "未获取到"))
        print("标题/描述：", video_info.get("desc", "未获取到"))
        print("封面链接：", video_info.get("video", {}).get("cover", {}).get("url_list", ["未获取到"])[0])

    except Exception as e:
        print(f"出错了：{e}")
    finally:
        # 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    get_douyin_info(douyin_url)