import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_models import FirstSource, SecondSource, Base

engine = create_engine('sqlite:///parser_news.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base.metadata.create_all(engine)
Base.metadata.bind = engine


def source_first():
    for i in range(10):
        url = f'https://www.sports.ru/boxing/news/?page={i}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        text = soup.find_all('strong')
        links = soup.find_all('a', class_='short-text', href=True)
        times = soup.find_all('span', class_='time')
        for i in range(len(text)):
            new_source = FirstSource(text=text[i].text.replace('/n', ''),
                                     url='https://www.sports.ru' + links[i]['href'].replace('/n', ''),
                                     time=times[i].text.replace('/n', ''))
            session.add(new_source)
            session.commit()


def source_second():
    for i in range(10):
        url = f'https://ua.tribuna.com/news/?page={i}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        text = soup.find_all('strong')
        links = soup.find_all('a', class_='short-text', href=True)
        times = soup.find_all('span', class_='time')
        for i in range(len(text)):
            new_source = SecondSource(text=text[i].text.replace('/n', ''),
                                      url='https://www.sports.ru' + links[i]['href'].replace('/n', ''),
                                      time=times[i].text.replace('/n', ''))
            session.add(new_source)
            session.commit()


if __name__ == '__main__':
    source_first()
    source_second()

