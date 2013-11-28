# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_operate_table = 'myf_operate'


class Myf_operate(Base):
    __tablename__ = myf_operate_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    browse_content = Column(String(512), nullable=False)
    user_id = Column(Integer, nullable=False)
    user_name = Column(String(20), nullable=False)
    browse_date = Column(DATETIME, nullable=False)
    ip_address = Column(String(20), nullable=False)