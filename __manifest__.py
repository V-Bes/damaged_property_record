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

    'depends': [
        'base',
        'mail',
    ],

    'data': [
        'security/dpr_groups.xml',
        'security/ir.model.access.csv',
        'security/dpr_security.xml',
        'data/dpr.city.csv',
        'data/dpr.position.csv',
        'data/dpr.owner.xml',
        'data/dpr.property.xml',
        'data/dpr.information.notice.xml',
        'data/dpr.application.xml',
        'data/dpr.invoice.xml',
        'report/hr_hospital_application_report.xml',
        'wizard/dpr_fill_out_checklist_wizard_view.xml',
        'views/dpr_menu.xml',
        'views/dpr_owner_views.xml',
        'views/dpr_property_views.xml',
        'views/dpr_information_notice_views.xml',
        'views/dpr_application_views.xml',
        'views/dpr_city_views.xml',
        'views/dpr_position_views.xml',
        'views/dpr_invoice_views.xml',
        'views/res_partner_view.xml',

    ],
    'demo': [

    ],
}
