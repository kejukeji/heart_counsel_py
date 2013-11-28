# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_ads_table = 'myf_ads'


class Myf_ads(Base):
    __tablename__ = myf_ads_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    url = Column(String(200), nullable=False)
    img_path = Column(String(255), nullable=False)
    typeid = Column(Integer, nullable=False)
    type = Column(Boolean, nullable=False)
    sort = Column(String(11), nullable=False)
    inputtime = Column(Integer, nullable=False)