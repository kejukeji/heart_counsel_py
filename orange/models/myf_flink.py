# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_flink_table = 'myf_flink'


class Myf_flink(Base):
    __tablename__ = myf_flink_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    sortrank = Column(Integer, nullable=False)
    url = Column(String(150), nullable=False)
    webname = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    logo = Column(String(150), nullable=True)
    dtime = Column(DATETIME, nullable=True)