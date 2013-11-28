# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_message_table = 'myf_message'


class Myf_message(Base):
    __tablename__ = myf_message_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    from_id = Column(Integer, nullable=True)
    to_id = Column(Integer, nullable=True)
    content = Column(String(50), nullable=True)
    message_type = Column(Integer, nullable=True)
    create_date = Column(DATETIME, nullable=True)
    create_by = Column(String(20), nullable=True)
    del_flag = Column(Integer, nullable=True)
    update_date = Column(DATETIME, nullable=True)
    update_by = Column(String(20), nullable=True)
    type = Column(Integer, nullable=False)