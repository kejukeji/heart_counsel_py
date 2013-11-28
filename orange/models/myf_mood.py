# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_mood_table = 'myf_mood'


class Myf_mood(Base):
    __tablename__ = myf_mood_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    title_id = Column(Integer, nullable=True)
    user_mood = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    user_name = Column(String(200), nullable=True)
    click_num = Column(Integer, nullable=True)
