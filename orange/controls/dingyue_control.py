# coding: UTF-8
from flask import request, render_template
from orange.services.dingyue_service import *

def show_dingyue():
    dingyue = get_dingyue()
    return render_template('dingyue.html',
                           dingyue=dingyue)