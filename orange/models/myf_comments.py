# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_comments_table = 'myf_comments'


class Myf_comments(Base):
    __tablename__ = myf_comments_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    article_test_id = Column(Integer, nullable= True)
    content=Column(String(200),nullable=False)
    user_id = Column(Integer, nullable= True)
    user_name=Column(String(20),nullable=False)
    comments_type = Column(Integer, nullable= True)
    del_flag = Column(Integer, nullable= False)
    create_date=Column(DATETIME,nullable=True)
    update_date=Column(DATETIME,nullable=False)
    update_by=Column(String(20),nullable=False)
    same = Column(Integer, nullable= False)