# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

gls_category_table = 'gls_category'


class Gls_category(Base):
    __tablename__ = gls_category_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    catid = Column(Integer, primary_key=True)
    siteid = Column(Integer, nullable=False, server_default='0')
    module = Column(String(15), nullable=False)
    type = Column(Boolean, nullable=False)
    modelid = Column(Integer, nullable=False, server_default='0')
    parentid = Column(Integer, nullable=False, server_default='0')
    arrparentid = Column(String(255), nullable=False)
    child = Column(Boolean, nullable=False)
    #arrchildid=Column(text(0),nullable=False)
    catname = Column(String(30), nullable=False)
    style = Column(String(5), nullable=False)
    image = Column(String(100), nullable=False)
    #description=Column(text(0),nullable=False)
    parentdir = Column(String(100), nullable=False)
    catdir = Column(String(30), nullable=False)
    url = Column(String(100), nullable=False)
    items = Column(Integer, nullable=False, server_default='0')
    hits = Column(Integer, nullable=False, server_default='0')
    #setting=Column(text(0),nullable=False)
    listorder = Column(Integer, nullable=False, server_default='0')
    ismenu = Column(Boolean, nullable=False)
    sethtml = Column(Boolean, nullable=False)
    letter = Column(String(30), nullable=False)
    usable_type = Column(String(255), nullable=False)