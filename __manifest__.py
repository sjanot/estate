{
    'name': 'Real estate',
    'version': '17.0.0.0',
    'summary': 'Real estate',
    'description': 'Real estate',
    'author': 'Štefan Janoťák',
    'website': 'https://www.symetra.sk/',
    'license': 'LGPL-3',
    'application': True,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'installable': True,
}
