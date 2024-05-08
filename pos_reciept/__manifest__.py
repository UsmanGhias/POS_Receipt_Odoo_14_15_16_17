{
    'name': 'POS Customization',
    'version': '16.0.0.0',
    'author': 'Muhamamd Abdullah',
    'category': 'Point Of Sale',
    'summary': 'Customized Receipt of Point Of Sales',
    'depends': ['base', 'point_of_sale'],
    "data": [
        'views/POS_changes.xml',
    ],
    'demo': [],
    'assets': {
       'point_of_sale.assets': [
                 'pos_reciept/static/src/xml/pos_reciept.xml',
                 'pos_reciept/static/src/js/customization.js',
                 'pos_reciept/static/src/css/pos_reciept.css'
       ],
 },
    'installable': True,
}