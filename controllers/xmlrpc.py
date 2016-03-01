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

service = Service(globals())


@service.xmlrpc
def add(a, b):
    return a + b


@service.xmlrpc
def sub(a, b):
    return a - b


def call():
    return service()


@service.xmlrpc
def user_test(test_user, test_user_pw, xmlrpc_user, xmlrpc_user_pw):

    import xmlrpclib

    uid = False

    xmlrpc_hostname = 'localhost'
    xmlrpc_sock_common_url = 'http://' + xmlrpc_hostname + ':8069/xmlrpc/common'
    xmlrpc_sock_str = 'http://' + xmlrpc_hostname + ':8069/xmlrpc/object'
    xmlrpc_dbname = 'clvhealth_biobox_dev'

    login_msg = ''
    user_name = ''
    company_name = ''

    try:
        sock_common = xmlrpclib.ServerProxy(xmlrpc_sock_common_url)
        uid = sock_common.login(xmlrpc_dbname, test_user, test_user_pw)
        sock = xmlrpclib.ServerProxy(xmlrpc_sock_str)
    except Exception:
        pass

    if uid is not False:
        pass
    else:
        login_msg = '[11] Server is not responding.'
        return \
            login_msg, \
            user_name, \
            company_name

    try:
        sock_common = xmlrpclib.ServerProxy(xmlrpc_sock_common_url)
        uid = sock_common.login(xmlrpc_dbname, xmlrpc_user, xmlrpc_user_pw)
        sock = xmlrpclib.ServerProxy(xmlrpc_sock_str)
    except Exception:
        pass

    if uid is not False:
        pass
    else:
        login_msg = '[21] Invalid Login/Pasword.'
        return \
            login_msg, \
            user_name, \
            company_name

    try:
        sock_common = xmlrpclib.ServerProxy(xmlrpc_sock_common_url)
        uid = sock_common.login(xmlrpc_dbname, xmlrpc_user, xmlrpc_user_pw)
        sock = xmlrpclib.ServerProxy(xmlrpc_sock_str)
    except Exception:
        pass

    user_fields = ['name', 'parent_id', ]
    user_data = sock.execute(xmlrpc_dbname, uid, xmlrpc_user_pw, 'res.users', 'read',
                             uid, user_fields)
    user_name = user_data['name']
    parent_id = user_data['parent_id'][0]

    args = [('id', '=', parent_id)]
    company_id = sock.execute(xmlrpc_dbname, uid, xmlrpc_user_pw, 'res.company', 'search', args)

    company_fields = ['name', ]
    company_data = sock.execute(xmlrpc_dbname, uid, xmlrpc_user_pw, 'res.company', 'read',
                                company_id[0], company_fields)
    company_name = company_data['name']

    if uid is not False:
        login_msg = '[01] Login Ok.'
        return \
            login_msg, \
            user_name, \
            company_name
