# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_hotyy_table = 'myf_hotyy'


class Myf_hotyy(Base):
    __tablename__ = myf_hotyy_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    arctype_id = Column(Integer, nullable=False)
    name = Column(String(50), nullable=False)
    allow_index_page = Column(Boolean, nullable=False)
    del_flag = Column(Boolean, nullable=False)
    create_date = Column(DATETIME, nullable=False)
    create_by = Column(String(50), nullable=False)
    update_date = Column(DATETIME, nullable=False)
    update_by = Column(String(50), nullable=False)
    orderid = Column(Integer, nullable=False)