{
    'name': 'Damaged property record',
    'author': 'Vladyslav Obyhvost',
    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '17.0.1.1.0',
    'support': 'vladioua@gmail.com',
    'website': 'https://odoo.school/',
    'images': ['static/description/icon.png'],
    'application': True,
    'installable': True,
    'auto_install': False,

    'data': [
        'security/ir.model.access.csv',
        'views/dpr_menu.xml',
        'views/dpr_owner_views.xml',
        'views/dpr_property_views.xml',
    ],
    'demo': [

    ],
}
