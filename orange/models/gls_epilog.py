# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

gls_epilog_table = 'gls_epilog'


class Gls_epilog(Base):
    __tablename__ = gls_epilog_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, nullable= False)
    start_score = Column(Integer, nullable= True)
    end_score = Column(Integer, nullable= False)
    #test_result = Column(text(0), nullable=False)
    create_date=Column(DATETIME,nullable=False)
    update_date=Column(DATETIME,nullable=False)
    create_by=Column(String(20),nullable=False)
    update_by=Column(String(20),nullable=False)
    del_flag = Column(Integer, nullable= False)
    img_path=Column(String(20),nullable=False)
