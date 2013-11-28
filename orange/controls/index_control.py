# coding: UTF-8
from flask import request, render_template
from orange.services.dingyue_service import *

def show_index():
    index = get_dingyue()
    return render_template('orange/index.html')