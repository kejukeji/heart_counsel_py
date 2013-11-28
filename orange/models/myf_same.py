# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_same_table = 'myf_same'


class Myf_same(Base):
    __tablename__ = myf_same_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    article_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)