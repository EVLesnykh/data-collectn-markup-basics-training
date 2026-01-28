# Код от преподавателя урезанная версия

# import scrapy
# class WikimediaSpider(scrapy.Spider):
#     name = 'wikimedia'
#     start_urls = ['https://commons.wikimedia.org/wiki/Category:Featured_pictures_on_Wikimedia_Commons']

#     def parse(self, response):
#         for image in response.xpath('//*[@id="mw-category-media"]/ul/li/div/span/a/img'):
#             image_url = image.xpath('@src').extract_first()
#             yield scrapy.Request(response.urljoin(image_url), self.save_image)

#     def save_image(self, response):
#         filename = response.url.split('/')[-1]

#         with open(f'images/{filename}', 'wb') as f:
#             f.write(response.body)

# File:"Everything_is_Going_to_be_Alright"_artwork,_Christchurch_Art_Gallery,_Christchurch,_New_Zealand.jpg

# Полная версия кода от преподавателя
import scrapy

class WikimediaSpider(scrapy.Spider):
    name = 'wikimedia'
    start_urls = ['https://commons.wikimedia.org/wiki/Category:Featured_pictures_on_Wikimedia_Commons']

    def parse(self, response):

        for image_page in response.xpath('//*[@id="mw-category-media"]/ul/li/div/a/@href').extract():

            yield scrapy.Request(response.urljoin(image_page), self.parse_image_page)

    def parse_image_page(self, response):

        full_image_url = response.xpath('//*[contains(@class, "fullImageLink")]/a/@href').extract_first()
        if full_image_url:

            yield scrapy.Request(response.urljoin(full_image_url), self.save_image)

    def save_image(self, response):

        filename = response.url.split('/')[-1]

        with open(f'images/{filename}', 'wb') as f:
            f.write(response.body)