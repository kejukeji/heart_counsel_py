# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_page_table = 'myf_page'


class Myf_page(Base):
    __tablename__ = myf_page_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    desc = Column(String(255), nullable=False)
    #content = Column(text(0), nullable=False)
    writer = Column(String(30), nullable=False)
    create_time = Column(DATETIME, nullable=False)