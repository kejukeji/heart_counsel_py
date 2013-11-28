# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_expression_table = 'myf_expression'


class Myf_expression(Base):
    __tablename__ = myf_expression_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    exp_num = Column(Integer, nullable=True)
    archives_id = Column(Integer, nullable=True)
    expression = Column(Integer, nullable=True)