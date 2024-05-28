# -*- coding: utf-8 -*-
{
    'name': "City Select",

    'summary': """
        This app is for City Select""",

    'description': """
        City Select
    """,

    'author': "Omer ABA",
    'website': "https://omeraba.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        
        'views/website_form.xml',
        
        
        
    ],
    # only loaded in demonstration mode
    'demo': [    ],
    'assets':{
        'web.assets_frontend': [
            'oao_select_city/static/src/js/form.js',
        ],
    },
}
