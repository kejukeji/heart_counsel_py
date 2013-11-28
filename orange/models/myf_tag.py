# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_tag_table = 'myf_tag'


class Myf_tag(Base):
    __tablename__ = myf_tag_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    arcid = Column(Integer, nullable=False)
    typeid = Column(Integer, nullable=True)
    createtime = Column(DATETIME, nullable=True)