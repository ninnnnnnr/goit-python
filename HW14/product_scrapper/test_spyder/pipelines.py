import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, relationship
from scrapy.exceptions import DropItem
from test_spyder.items import SpyderItem



DB = declarative_base()
authors_quotes_association = Table('author_quote', DB.metadata,
                                   Column('author_id', Integer, ForeignKey('author.id')),
                                   Column('quote_id', Integer, ForeignKey('quote.id'))
                                   )


class Author(DB):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    author = Column(String)
    url = Column(String)

    def __init__(self, author, url):
        self.author = author
        self.url = url

    def __repr__(self):
        return self.author, self.url


class Quote(DB):
    __tablename__ = 'quote'
    id = Column(Integer, primary_key=True)
    quote = Column(String)
    keywords = Column(String)
    author = relationship("Author", secondary=authors_quotes_association)

    def __init__(self, quote, keywords):
        self.quote = quote
        self.keywords = keywords

    def __repr__(self):
        return self.quote, self.keywords


class SpyderPipeline(object):
    def __init__(self):
        basename = 'database'
        self.engine = create_engine("sqlite:///%s" % basename, echo=False)
        if not os.path.exists(basename):
            DB.metadata.create_all(self.engine)
        self.authors = set()

    def process_item(self, item, spider):
        if isinstance(item, SpyderItem):
            authors = item['author'] + item['url']
            if authors not in self.authors:
                dt = Author(item['author'], item['url'])
                self.authors.add(authors)
                self.session.add(dt)
        elif isinstance(item, SpyderItem):
            dt = Quote(item['quote'], item['keywords'])
            self.session.add(dt)
        return item

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()

    def open_spider(self, spider):
        self.session = Session(bind=self.engine)


class DuplicatesPipeline(object):
    def __init__(self):
        self.authors = set()

    def process_item(self, item, spider):
        if isinstance(item, SpyderItem):
            authors = item['author'] + item['url']
            if authors in self.authors:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.authors.add(item['id'])
                return item
        else:
            return item
