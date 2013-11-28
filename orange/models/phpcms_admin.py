# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

phpcms_admin_table = 'phpcms_admin'


class Phpcms_admin(Base):
    __tablename__ = phpcms_admin_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    userid = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    allowmultilogin = Column(Boolean, nullable=False)
    alloweditpassword = Column(Boolean, nullable=False)
    editpasswordnextlogin = Column(Boolean, nullable=False)
    disabled = Column(Boolean, nullable=False)