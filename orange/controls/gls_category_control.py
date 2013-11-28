# coding: UTF-8
from flask import request, render_template
from orange.services.gls_category_service import *

def show_gls_category():
    gls_category = get_gls_category()
    return render_template('gls_category.html',
                           gls_category=gls_category)