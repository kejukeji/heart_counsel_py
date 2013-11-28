# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_admin_role_table = 'myf_admin_role'


class Myf_admin_role(Base):
    __tablename__ = myf_admin_role_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    rolename = Column(String(50), nullable=False)
    #description = Column(text(0), nullable=False)
    disabled = Column(Boolean, nullable=False)