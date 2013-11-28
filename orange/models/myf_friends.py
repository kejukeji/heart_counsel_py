# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_friends_table = 'myf_friends'


class Myf_friends(Base):
    __tablename__ = myf_friends_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=True)
    friend_id = Column(Integer, nullable=True)
    state = Column(Integer, nullable=True)
    del_flag = Column(Boolean, nullable=True)
    create_date = Column(DATETIME, nullable=True)
    create_by = Column(String(20), nullable=True)
    update_date = Column(DATETIME, nullable=True)
    update_by = Column(String(20), nullable=True)
