# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_dingyue_table = 'myf_dingyue'


class Myf_dingyue(Base):
    __tablename__ = myf_dingyue_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)