# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_statistics_table = 'myf_statistics'


class Myf_statistics(Base):
    __tablename__ = myf_statistics_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    article_test_id = Column(Integer, nullable=True)
    reproduce_num = Column(Integer, nullable=True)
    comment_num = Column(Integer, nullable=True)
    collection_num = Column(Integer, nullable=True)
    brower_num = Column(Integer, nullable=False)
    exact_num = Column(Integer, nullable=False)
    forbid_num = Column(Integer, nullable=False)
    create_date = Column(DATETIME, nullable=True)
    create_by = Column(String(20), nullable=True)
    del_flag = Column(Integer, nullable=True)
    type = Column(Integer, nullable=True)