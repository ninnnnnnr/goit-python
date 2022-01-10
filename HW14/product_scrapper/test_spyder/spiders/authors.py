import scrapy
from test_spyder.items import SpyderItem


class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            Item = SpyderItem()
            Item['keywords'] = quote.xpath("div[@class='tags']/a/text()").extract()
            Item['author'] = quote.xpath("span/small/text()").extract_first()
            Item['quote'] = ''.join(value.strip('"') for value in quote.xpath("span[@class='text']/text()")
                                    .extract_first()).replace("\n","")
            Item['url'] = 'quotes.toscrape.com' + quote.xpath("span/a/@href").extract_first()
            yield Item

            next_link = response.xpath("//li[@class='next']/a/@href").get()
            if next_link:
                yield scrapy.Request(url=self.start_urls[0] + next_link)
