{
    'name': 'Estate',
    'version': '1.0',
    'summary': 'Module Estate',
    'description': """
Estate Property
=================
Module Estate provide management solution.
""",
    'category': 'Estate',
    'depends': ['base'],
    'data': [
        'data/demo.xml',
        'data/res_groups.xml',
        'views/estate_property_views.xml',
        'views/estate_menu.xml', 
        'security/ir.model.access.csv',
    ],
    
    
    'installable': True,
    'application': True,
}
