# coding: UTF-8
from flask import request, render_template
from orange.services.gls_epilog_service import *

def show_gls_epilog_service():
    gls_epilog = get_gls_epilog()
    return render_template('gls_epilog.html',
                           gls_epilog=gls_epilog)