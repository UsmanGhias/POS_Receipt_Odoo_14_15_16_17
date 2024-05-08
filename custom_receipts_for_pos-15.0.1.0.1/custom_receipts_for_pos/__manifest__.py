{
    'name': 'Custom Receipts for POS',
    'version': '15.0.1.0.1',
    'summary': "Add Custom Receipt for each POS",
    'description': "It helps to create and select customised receipts for "
                   "each POS",
    'category': 'Point of Sale',
    'author': 'UsmanGhias',
    'company': 'TeleNoc',
    'maintainer': 'TeleNoc ORG',
    'website': "https://www.telenoc.org",
    'depends': ['base', 'point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/point_of_sale_view.xml',
        'views/pos_receipt_views.xml',
        'views/pos_config_views.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'custom_receipts_for_pos/static/src/js/ReceiptScreen/order_receipt.js',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
