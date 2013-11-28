# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_archive_click_table = 'myf_archive_click'


class Myf_archive_click(Base):
    __tablename__ = myf_archive_click_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    archive_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=True)
    click_date = Column(DATETIME, nullable=False)