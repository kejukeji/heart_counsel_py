# coding: UTF-8
from flask import request, render_template
from orange.services.myf_archives_service import *

def show_myf_archives():
    myf_archives_self = get_myf_archives_self()
    return render_template('/default/secret/self.html',
                           myf_archives_self=myf_archives_self)