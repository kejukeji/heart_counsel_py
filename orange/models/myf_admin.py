# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_admin_table = 'myf_admin'


class Myf_admin(Base):
    __tablename__ = myf_admin_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    userid = Column(String(30), nullable=False)
    pwd = Column(String(32), nullable=False)
    uname = Column(String(30), nullable=True)
    email = Column(String(50), nullable=False)
    logintime = Column(DATETIME, nullable=True)
    loginip = Column(String(20), nullable=True)
    createtime = Column(DATETIME, nullable=True)
    roleid = Column(Integer, nullable=True)