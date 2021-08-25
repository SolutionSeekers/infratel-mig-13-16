# -*- coding: utf-8 -*-
{
    'name': "Empresa",

    'summary': """
        Empresa customizations module
    """,

    'description': """
        Coparmex customizations module
    """,

    'author': "Indboo",
    'website': "https://indboo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        # Mexican accounting
        # Installed apps
        'account',
        # 'hr_holidays'
        ],
    # always loaded
    'data': [
        'reports/account_invoice_report.xml',
	],
    # only loaded in demonstration mode
    'demo': [
    ],
}

