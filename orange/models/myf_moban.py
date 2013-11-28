# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_moban_table = 'myf_moban'


class Myf_moban(Base):
    __tablename__ = myf_moban_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    filename = Column(String(255), nullable=True)
    name = Column(String(50), nullable=True)
    updatetime = Column(DATETIME, nullable=True)