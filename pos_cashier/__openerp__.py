# -*- coding: utf-8 -*-
{
    'name': "POS Cashiers",

    'summary': "Gestion des cassiers pour le point de vente",

    'description': "Gestion des cassiers pour chaque point de vente",

    'author': "Junior Djapou",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point Of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/pos_cashier_security.xml',
        'templates.xml',
        'cashier_view.xml',
        'order_cashier_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'js': [
        'static/src/js/pos_cashier.js',
    ],
    'css': [
        'static/src/css/pos_cashier.css',
    ],
    'qweb': [
        'static/src/xml/pos_cashier.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}