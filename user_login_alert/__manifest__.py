# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Niyas Raphy(v11) and Akshay Babu(v12)(<https://www.cybrosys.com>)(odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'User Login Alert',
    'summary': """Secure your Odoo account by alerts at right time. If any successful login to your
                account happens, an alert mail will be send to you with the browser and IP details.""",
    'version': '13.0.1.0.0',
    'description': """Secure your Odoo account by alerts at right time. If any successful login to your
                    account happens, an alert mail will be send to you with the browser and IP details, Odoo 13, Odoo13""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'category': 'Tools',
    'depends': ['base', 'mail'],
    'license': 'AGPL-3',
    'data': [
        'security/notification_group.xml',
        'views/logged_details_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'external_dependencies': {
        'python': ['httpagentparser'],
    },


}

