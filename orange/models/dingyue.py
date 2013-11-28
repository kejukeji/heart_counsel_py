# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

dingyue_table = 'dingyue'


class Dingyue(Base):
    __tablename__ = dingyue_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    times = Column(String(20), nullable=False)