# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_reproduce_table = 'myf_reproduce'


class Myf_reproduce(Base):
    __tablename__ = myf_reproduce_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    article_test_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=True)
    user_name = Column(String(20), nullable=True)
    create_date = Column(DATETIME, nullable=False)
    reproduce_type = Column(Integer, nullable=False)