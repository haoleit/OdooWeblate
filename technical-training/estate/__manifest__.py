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
    'depends': ['base',
                'website',
                'web',
                'mail',
                'report_xlsx'],
    'data': [
        'data/demo.xml',
        'data/menu_data.xml',
        'data/res_groups.xml',
        'data/sequence.xml',
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/demo_widget_views.xml',
        'views/estate_templates.xml',
        'views/bemo_templates.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_user_views.xml',
        'views/feedback_views.xml',
        'views/snippets/snippet_feedback.xml',
        "wizards/report_buyer_offers_xlsx.xml",
        'reports/report_buyer_offer_views.xml',
        'reports/report.xml',
        'views/estate_menu.xml', 
    ],
    'qweb':[
        'static/src/xml/*.xml'
    ],
    
    'installable': True,
    'application': True,
}
