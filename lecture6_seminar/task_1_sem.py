# Задание 1

# - Создайте новый проект Scrapy с именем "wikimedia_scraper".
# - В каталоге spiders создайте нового паука с именем "wikimedia".
# - Определите start_urls равным
# https://commons.wikimedia.org/wiki/Category:Featured_pictures_on_Wikimedia_Commons
# - Создайте метод parse в пауке, который будет извлекать URL отдельных страниц изображений 
# со страницы категории.
# - Создайте метод parse_image, который будет использоваться для парсинга отдельных страниц изображений.

# Подсказки:
# - Используйте выражение xpath в методе парсинга для извлечения URL-адресов.
#  Например: response.xpath("//li[@class='gallerybox']/div/div/div/a/@href").extract()
# - Используйте метод response.follow() для перехода по каждому извлеченному URL 
# к соответствующей странице изображения и передайте его в метод parse_image.