# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_rubbish_table = 'myf_rubbish'


class Myf_rubbish(Base):
    __tablename__ = myf_rubbish_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    del_time = Column(DATETIME, nullable=True)
    del_user = Column(Integer, nullable=False)
    type = Column(String(2), nullable=False)
    #content = Column(text(0), nullable=True)