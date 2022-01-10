from scrapy.item import Item, Field

class SpyderItem(Item):
    keywords = Field()
    author = Field()
    quote = Field()
    url = Field()
