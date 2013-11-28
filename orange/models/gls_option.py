# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

gls_option_table = 'gls_option'


class Gls_option(Base):
    __tablename__ = gls_option_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    problem_id = Column(Integer, nullable= False)
    answer=Column(String(200),nullable=False)
    score = Column(Integer, nullable= False)
    theme_id = Column(Integer, nullable= False)
    del_flag = Column(Integer, nullable= False)
    create_date=Column(DATETIME,nullable=False)
    update_date=Column(DATETIME,nullable=False)
    create_by=Column(String(20),nullable=False)
    update_by=Column(String(20),nullable=False)
    litpics=Column(String(255),nullable=False)
