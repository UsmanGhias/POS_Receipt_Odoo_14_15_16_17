{
    'name': 'Custom Receipts For POS',
    'version': '15.0.1.0.0',
    'category': 'Point of Sale',
    'summary': """Customizable receipt for POS""",
    'description': """
        This module is used to select customized receipts for POS.
        Update and tested for Odoo 15.
    """,
    'author': 'Usman Ghias',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc',
    'website': "https://www.telenoc.org",
    'depends': ['base', 'point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/pos_receipt_data.xml',
        'views/pos_receipt_views.xml',
        'views/pos_config_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_receipts_for_pos/static/src/js/pos_receipt.js',
        ],
        'web.assets_qweb': [
            'custom_receipts_for_pos/static/src/xml/pos_receipt.xml',
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
