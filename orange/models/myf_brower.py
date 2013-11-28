# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_brower_table = 'myf_brower'


class Myf_brower(Base):
    __tablename__ = myf_brower_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    browse_content = Column(String(200), nullable=True)
    user_id = Column(Integer, nullable=True)
    user_name = Column(String(20), nullable=True)
    browse_date = Column(DATETIME, nullable=True)