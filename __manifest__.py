{
    'name': 'Passport',
    'category': 'Sales/CRM',
    'sequence': 350,
    'summary': 'Add Passport Fields',
    'description': """
This module adds passport fields to include in contact registers.
""",
    'depends': ['contacts'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}