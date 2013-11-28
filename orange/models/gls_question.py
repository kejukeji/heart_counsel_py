# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

gls_question_table = 'gls_question'


class Gls_question(Base):
    __tablename__ = gls_question_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, nullable= False)
    title=Column(String(255),nullable=False)
    option_type = Column(Integer, nullable= False)
    series_num = Column(Integer, nullable= False)
    del_flag = Column(Integer, nullable= False)
    create_date=Column(DATETIME,nullable=False)
    update_date=Column(DATETIME,nullable=False)
    create_by=Column(String(20),nullable=False)
    update_by=Column(String(20),nullable=False)
    ti_img=Column(String(200),nullable=False)
