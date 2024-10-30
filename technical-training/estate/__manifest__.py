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
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menu.xml', 
    ],
    
    
    'installable': True,
    'application': True,
}
