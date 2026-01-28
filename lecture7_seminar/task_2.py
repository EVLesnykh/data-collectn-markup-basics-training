from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_options)

youtube_channel_url = "https://www.youtube.com/@progliveru/videos"

try:
    driver.get(youtube_channel_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    page_height = driver.execute_script("return document.documentElement.scrollHeight")
    scroll_pause_time = 2
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == page_height:
            break
        page_height = new_height

    video_titles_xpath = "//*[@id='video-title-link']"
    metadata_xpath = "//div[@id='metadata-line']/span[1]"

    video_titles = driver.find_elements(By.XPATH, video_titles_xpath)
    metadata_elements = driver.find_elements(By.XPATH, metadata_xpath)

    video_data = {}
    for i in range(min(len(video_titles), len(metadata_elements))):
# Цикл for проходит по индексам от 0 до минимальной длины между списками
# video_titles и metadata_elements.
# Это делается для того, чтобы избежать ошибок, если списки разной длины.

          title = video_titles[i].text
# Извлекается текстовый контент из элемента video_titles по текущему индексу i и сохраняется в переменную title.

          metadata_text = metadata_elements[i].text
# Извлекается текстовый контент из элемента metadata_elements по текущему индексу i и сохраняется в переменную metadata_text.


          if "•" in metadata_text:
              views, time_ago = metadata_text.split("•")
# Если в metadata_text содержится символ "•", строка разбивается на две части по этому символу.
# Первая часть сохраняется в переменную views, вторая часть - в time_ago.

          else:
              views = metadata_text
              time_ago = "Неизвестно"
# Если символа "•" нет, вся строка сохраняется в переменную views.
# Переменная time_ago устанавливается в значение "Неизвестно".

          video_data[title] = {"views": views.strip(), "published": time_ago.strip()}

    print(video_data)

except Exception as e:
    print("Произошла ошибка:", e)

finally:
    driver.quit()