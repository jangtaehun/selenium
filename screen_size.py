from selenium import webdriver
import time
from math import ceil

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# selenium search element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# search - tag
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# option to be kept open
options = Options()
options.add_experimental_option("detach", True)  # 자동 꺼짐 방지


class ResponsiveTester:
    def __init__(self, urls):
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [360, 480, 960, 1024]

    def screenshot(self, url):
        browser_height = 875  # self.browser.get_window_size()
        self.browser.get(url)
        for size in self.sizes:
            self.browser.set_window_size(size, browser_height)
            self.browser.execute_script(
                "window.scrollTo(0,0)"
            )  # 사이즈 바뀔 때 마다 상단으로 이동
            time.sleep(3)
            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight"
            )
            # javascript function을 호출해 return한 다음 높이를 얻는다.
            total_sections = ceil(scroll_size / browser_height)
            # document의 높이를 브라우저의 높이로 나누면 스크롤을 몇 번 해야하는 지 알 수 있다.
            for section in range(total_sections):
                self.browser.execute_script(
                    f"window.scrollTo(0, {(section+1)*browser_height})"
                )
                self.browser.save_screenshot(f"{size}x{section+1}.png")
                time.sleep(2)

    def start(self):
        for url in self.urls:
            self.screenshot(url)


screen = ResponsiveTester(["https://nomadcoders.co/kokoa-clone"])
screen.start()
