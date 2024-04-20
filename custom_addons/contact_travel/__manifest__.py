# -*- coding: utf-8 -*-
{
    'name': "Contact travel",
    'summary': """ Contact travel """,

    'version'       : "16.0.0",
    'category'      : "//",

    "contributors": [
        "Meftouh Mohamed Adda",
    ],
    
    'sequence': 1,
    
    'company'       : 'Weasydoo',
    'author'        : 'Meftouh Mohamed Adda',
    'maintainer'    : 'Weasydoo',

    'website': "https://github.com/MohamedMeftouh21",
    'support' : "//",


    'depends': [
        'base',
    ],
    
    'data': [

        'security/ir.model.access.csv',
     'views/voyage.xml',
       'views/res_partner_view.xml',

       'views/menu_item.xml',

    ],



    'license'       : "LGPL-3",
    'price'         : "0",
    'currency'      : 'Eur',

  

    'installable': True,
    'auto_install': False,
    'application': True,
}