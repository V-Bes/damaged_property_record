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
        'views/damaged_property_menu.xml',
        'views/damaged_property_owner_views.xml',

    ],
    'demo': [

    ],
}
