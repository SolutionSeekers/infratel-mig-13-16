# -*- coding: utf-8 -*-
{
    'name': "Juarez Technology",

    'summary': """
        Mexico address format (Colony field)
    """,

    'description': """
        Mexico address format (Colony field)
    """,

    'author': "Juarez Technology",
    'website': "https://juarez.technology",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        # Mexican accounting
        # Installed apps
        'l10n_mx_edi'
        # 'hr_holidays'
        ],
    # always loaded
    'data': [
	],
    # only loaded in demonstration mode
    'demo': [
    ],
}

