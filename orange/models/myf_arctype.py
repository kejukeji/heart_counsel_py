# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_arctype_table = 'myf_arctype'


class Myf_arctype(Base):
    __tablename__ = myf_arctype_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    topid = Column(Integer, nullable=False)
    sortrank = Column(Integer, nullable=False)
    typename = Column(String(50), nullable=False)
    typedir = Column(String(50), nullable=False)
    arcnamerule = Column(String(50), nullable=True)
    listnamerule = Column(String(50), nullable=True)
    indexpath = Column(String(255), nullable=True)
    listpath = Column(String(255), nullable=True)
    singlepath = Column(String(255), nullable=True)
    archivepath = Column(String(255), nullable=True)
    keywords = Column(String(255), nullable=True)
    seotitle = Column(String(255), nullable=True)
    description = Column(String(1600), nullable=True)
    typepro = Column(Integer, nullable=False)
    dirpos = Column(Integer, nullable=True)
    isshow = Column(Integer, nullable=True)
    litpic = Column(String(255), nullable=True)
    #body = Column(text(0), nullable=True)
    enname = Column(String(50), nullable=True)


