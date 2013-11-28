# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_cheng_tu_table = 'myf_cheng_tu'


class Myf_cheng_tu(Base):
    __tablename__ = myf_cheng_tu_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    url = Column(String(200), nullable=False)
    description = Column(String(255), nullable=False)
    inputtime = Column(DATETIME, nullable=False)
    img_path = Column(String(200), nullable=False)
    is_what = Column(Boolean, nullable=False)