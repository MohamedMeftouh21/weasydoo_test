# -*- coding: utf-8 -*-
{
    'name': "contact_travel",
    'summary': """ Contact travel """,

    'version': '1.0',
    'category': 'ContactTravel',

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
        'contacts'
    ],
    
    'data': [

        'security/ir.model.access.csv',
     'views/voyage.xml',
       'views/res_partner_view.xml',

       'views/menu_item.xml',

    ],



    'license'       : "LGPL-3",
    'price'         : "0",
    'currency'      : 'DA',

  

    'installable': True,
    'auto_install': False,
    'application': True,
}