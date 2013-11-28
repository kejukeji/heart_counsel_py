# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_admin_priv_table = 'myf_admin_priv'


class Myf_admin_priv(Base):
    __tablename__ = myf_admin_priv_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)
    m = Column(String(40), nullable=False)
    c = Column(String(40), nullable=True)
    a = Column(String(40), nullable=True)
    data = Column(String(), nullable=True)