# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_archives_table = 'myf_archives'


class Myf_archives(Base):
    __tablename__ = myf_archives_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    typeid = Column(Integer, nullable=False)
    typename = Column(String(50), nullable=True)
    flag = Column(String(50), nullable=True)
    click= Column(Integer, nullable=True)
    title = Column(String(255), nullable=False)
    color = Column(String(7), nullable=True)
    writer = Column(String(50), nullable=True)
    source = Column(String(50), nullable=True)
    jump = Column(String(255), nullable=True)
    litpic = Column(String(255), nullable=True)
    smallpic = Column(String(255), nullable=True)
    tag = Column(String(255), nullable=True)
    keywords = Column(String(255), nullable=True)
    description = Column(String(500), nullable=True)
    sendtime = Column(DATETIME, nullable=False)
    adminid = Column(Integer, nullable=True)
    adminname = Column(String(30), nullable=True)
    #body = Column(text, nullable=True)
    ishtml = Column(Boolean, nullable=False)
    type = Column(String(30), nullable=False)
    del_flag = Column(Integer, nullable=True)
    page_num = Column(Integer, nullable=False)
    same_num = Column(Integer, nullable=False)
    ddy = Column(Integer, nullable=False)
