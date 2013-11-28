# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_home_flash_table = 'myf_home_flash'


class Myf_home_flash(Base):
    __tablename__ = myf_home_flash_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    #content = Column(text(0), nullable=False)
    writer = Column(String(50), nullable=False)
    inputtime = Column(DATETIME, nullable=False)