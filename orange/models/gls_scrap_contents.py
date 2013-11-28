# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

gls_scrap_contents_table = 'gls_scrap_contents'


class Gls_scrap_contents(Base):
    __tablename__ = gls_scrap_contents_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    arctype_id = Column(Integer, nullable=False)
    img_path = Column(String(100), nullable=False)
    contents = Column(String(250), nullable=False)
    del_flag = Column(Boolean, nullable=False)
    create_date = Column(DATETIME, nullable=False)
    create_by = Column(String(50), nullable=False)
    update_date = Column(DATETIME, nullable=False)
    update_by = Column(String(50), nullable=False)
