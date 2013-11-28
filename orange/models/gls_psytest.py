#coding: utf-8
from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

gls_psytest_table = 'gls_psytest'


class Gls_psytest(Base):
    __tablename__ = gls_psytest_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    column_id = Column(Integer, nullable=False)
    title = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    image_path = Column(String(80), nullable=False)
    title_num = Column(Integer, nullable=False)
    question_type = Column(Integer, nullable=False)
    create_date = Column(DATETIME, nullable=False)
    create_by = Column(String(50), nullable=False)
    update_date = Column(DATETIME, nullable=False)
    update_by = Column(String(50), nullable=True)
    del_flag = Column(Integer, nullable=False)
    columns = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    order = Column(Integer, nullable=False)
    orderr = Column(Integer, nullable=False)
    keywords = Column(String(255), nullable=True)
    source = Column(String(30), nullable=True)
    status = Column(Boolean, nullable=False)
    click = Column(Integer, nullable=False)
