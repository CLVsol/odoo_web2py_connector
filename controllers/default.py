# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2016-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

from __future__ import print_function

from gluon.tools import Service

URL_ERROR = URL('default', 'error')


def index():
    return 'Odoo web2py Connector'


def error():
    # print('>>>>>', 'There is an error!')
    return H1('There is an error!')


def sum():
    # http://ubun14:8000/odoo_web2py_connector/default/sum/4/8
    # print(request.args)
    x = request.args(0)
    y = request.args(1)
    if not all([x, y]):
        redirect(URL_ERROR)
    return int(x) + int(y)


def sum2():
    # http://ubun14:8000/odoo_web2py_connector/default/sum2/?x=4&y=8
    # print(request.vars)
    x = request.vars['x'] or redirect(URL_ERROR)
    y = request.vars.y or redirect(URL_ERROR)
    return int(x) + int(y)

service = Service(globals())


@service.xmlrpc
def add(a, b):
    return a + b


@service.xmlrpc
def sub(a, b):
    return a - b


def call():
    return service()
