# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_honor_list_table = 'myf_honor_list'


class Myf_honor_list(Base):
    __tablename__ = myf_honor_list_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)