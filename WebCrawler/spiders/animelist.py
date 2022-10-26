import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsAnimelistSpider
from WebCrawler.pipelines import Database


class AnimelistSpider(scrapy.Spider):
    name = 'animelist'
    allowed_domains = ['myanimelist.net']
    start_urls = [
        f'https://myanimelist.net/manga.php?letter=A']
    Database.connectDb()
    Database.createTable()

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_anime)

    def parse_anime(self, response):
        liste_anime = response.css('tr')[8:]

        for anime in liste_anime:
            item = ReviewsAnimelistSpider()

            try:
                item['title'] = anime.css('strong::text').extract()[0]
            except:
                item['title'] = 'None'

            try:
                item['img'] = anime.css('img').attrib['data-src']
            except:
                item['img'] = 'None'

            try:
                item['desc'] = anime.css('div.pt4::text').extract()[0]
            except:
                item['desc'] = 'None'

            Database.addRow(item)

            yield item
