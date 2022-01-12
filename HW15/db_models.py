from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class FirstSource(Base):
    __tablename__ = "first_source"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    url = Column(String)
    time = Column(String)


class SecondSource(Base):
    id = Column(Integer, primary_key=True)
    __tablename__ = "second_source"
    text = Column(String)
    url = Column(String)
    time = Column(String)

