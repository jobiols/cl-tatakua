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
    'version': '13.0.0.0',
    'category': 'Tools',
    'summary': "Proyecto Tatakua",
    'author': "Tecnopro",
    'website': 'http://github.com/jobiols/cl-tatakua',
    'license': 'AGPL-3',
    'depends': [
        'l10n_py_vat_book',
        'partner_ruc_unique',

        # multiples medios de pago
        'account_payment_group',
        # cartera de cheques e imporesion de cheques
        'l10n_py_check_printing',
    ],
    'data': [
    ],
    'installable': True,
    'application': False,

    'limit_request': '8196',
    'limit_memory_soft': '640000000',
    'limit_memory_hard': '760000000',
    'limit_time_cpu': '60',
    'limit_time_real': '120',

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'EE',

    # port where odoo starts serving pages
    'port': '8069',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'https://github.com/jobiols/cl-tatakua.git',
        'git@github.com:jobiols/odoo-paraguay.git',
        'https://github.com/jobiols/odoo-addons.git',

        # para multiple medios de pago
        'https://github.com/jobiols/adhoc-account-payment.git',
        'https://github.com/jobiols/adhoc-account-financial-tools.git',
    ],

    'docker-images': [
        'odoo jobiols/odoo-ent:13.0e',
        'postgres postgres:10.1-alpine',
        'nginx nginx'
    ]
}
