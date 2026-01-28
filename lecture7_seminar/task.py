from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# класс для указания типа селектора
from selenium.webdriver.common.by import By
# класс для ожидания наступления события
from selenium.webdriver.support.ui import WebDriverWait
# включает проверки, такие как видимость элемента на странице,
# доступность элемента для клика и так далее.
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
#chrome_options.add_argument('--ignore-certificate-errors-spki-list')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.youtube.com/@progliveru/videos")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.TAG_NAME, 'body'))
)

scroll_pause = 2
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(scroll_pause)
    page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if last_height == page_height:
      break

    last_height = page_height
print(f'Высота last_height: {last_height}')


print(f'Высота: {page_height}')

driver.quit()
