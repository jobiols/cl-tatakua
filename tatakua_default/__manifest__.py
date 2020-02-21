##############################################################################
#
#    Copyright (C) 2019  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Tatakua',
    'version': '13.0e.0.0.0',
    'category': 'Tools',
    'summary': "Instancia Tatakua",
    'author': "Tecnopro",
    'website': 'http://github.com/jobiols/cl-tatakua',
    'license': 'AGPL-3',
    'depends': [
        'l10n_py_vat_book',
        'partner_ruc_unique'
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    'port': '8069',
    'repos': [
        {'usr': 'jobiols', 'repo': 'cl-tatakua', 'branch': '13.0'},
        {'usr': 'jobiols', 'repo': 'odoo-paraguay', 'branch': '13.0'},
        {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '13.0'},
        {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '13.0'},
    ],
    'docker': [
        {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-ent', 'ver': '13.0e'},
        {'name': 'postgres', 'usr': 'postgres', 'ver': '10.1-alpine'},
        {'name': 'nginx', 'usr': 'nginx', 'ver': 'latest'},
    ]

}
