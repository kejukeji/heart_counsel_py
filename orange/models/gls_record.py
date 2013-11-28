# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

gls_record_table = 'gls_record'


class Gls_record(Base):
    __tablename__ = gls_record_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    gls_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)
    test_result = Column(String(200), nullable=False)
    create_date = Column(DATETIME, nullable=False)