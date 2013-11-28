# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_newtopic_table = 'myf_newtopic'


class Myf_newtopic(Base):
    __tablename__ = myf_newtopic_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    img_path = Column(String(120), nullable=False)
    arcurl = Column(String(120), nullable=False)
    #content = Column(text(0), nullable=True)
    createtime = Column(DATETIME, nullable=True)