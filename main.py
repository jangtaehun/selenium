from selenium import webdriver
import time

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


class GoogleKeywordScreenshooter:
    def __init__(self, KEYWORD, screenshot_dir):
        self.browser = webdriver.Chrome(options=options)
        self.keyword = KEYWORD
        self.screenshot_dir = screenshot_dir

    def start(self):
        self.browser.get("https://google.com")
        # search - bar
        search_bar = self.browser.find_element(By.CLASS_NAME, "gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)

        # 구글에서 검색하고 selenium이 inspect하는 시간이 짧아서 요소를 읽어 올 수 없다
        search_results = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "g"))
        )

        # screen shot
        # enumerate: index도 가져온다.
        for index, search_result in enumerate(search_results):
            time.sleep(1)
            search_result.screenshot(
                f"{self.screenshot_dir}/{self.keyword}X{index}.png"
            )

    def finish(self):
        self.browser.quit()


domain_competitiors = GoogleKeywordScreenshooter("buy domain", "screenshots")
domain_competitiors.start()
domain_competitiors.finish()
python_competitiors = GoogleKeywordScreenshooter("python book", "screenshots")
python_competitiors.start()
python_competitiors.finish()

"""
# print text
for search_result in search_results:
    title = search_result.find_element(By.TAG_NAME, "h3")
    if title:
        print(title.text)
"""


# search_results = WebDriverWait(browser, 10).until(
#     EC.presence_of_all_elements_located((By.CLASS_NAME, "Ww4FFb"))
# )
# for index, search_result in enumerate(search_results):
#     time.sleep(2)
#     class_name = search_result.get_attribute("class")
#     if (
#         "G8qI4b" not in class_name
#     ):  # Ww4FFb를 포함한 클레스 중에서 G8qI4b가 없는 클레스를 출력
#         search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")
