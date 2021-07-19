# noinspection PyStatementEffect
{
    'name': "Multi Company Email / Multi Company Signature",

    'sequence': 202,

    'summary': """ Changes user's email and signature to the ones defined in the current company """,

    'author': "Arxi",
    'website': "http://www.arxi.pt",

    'category': 'Extra Tools',
    'version': '13.0.1.0.2',
    'license': 'OPL-1',

    'price': 89.00,
    'currency': 'EUR',

    'depends': ['base', 'mail'],

    'data': [
        'views/templates.xml',
    ],

    'images': [
        'static/description/banner.png',
    ],

    'application': True,
    'installable': True,
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook'
}
