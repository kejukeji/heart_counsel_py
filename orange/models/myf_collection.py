# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_collection_table = 'myf_collection'


class Myf_collection(Base):
    __tablename__ = myf_collection_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    article_test_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    user_name = Column(String(20), nullable=False)
    create_date = Column(DATETIME, nullable=True)
    collection_type = Column(Integer, nullable=True)