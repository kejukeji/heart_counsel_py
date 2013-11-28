# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_type_table = 'myf_type'


class Myf_type(Base):
    __tablename__ = myf_type_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    typename = Column(String(30),nullable=False)
    typecontent = Column(String(255),nullable=False)