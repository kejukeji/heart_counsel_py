# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_user_honor_table = 'myf_user_honor'


class Myf_user_honor(Base):
    __tablename__ = myf_user_honor_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    user_id = Column(Integer, primary_key=True)
    honor_id = Column(Integer, primary_key=True)