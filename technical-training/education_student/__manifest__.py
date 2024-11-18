# __manifest__.py
{
    'name': 'Education Student View',
    'version': '1.0',
    'category': 'Education',
    'depends': ['base', 'web'],
    'data': [
        'data/student_data.xml',
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/student_views.xml',
        'views/student_menu.xml'
    ],
    'qweb':[
        'static/src/xml/*.xml'
    ],
    'installable': True,
    'application': True,
}
