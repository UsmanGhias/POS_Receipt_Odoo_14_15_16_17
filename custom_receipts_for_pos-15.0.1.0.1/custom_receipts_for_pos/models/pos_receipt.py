from odoo import fields, models


class PosReceipt(models.Model):
    _name = 'pos.receipt'
    _description = 'POS Receipt'

    """models that helps to create new custom receipts for POS"""

    name = fields.Char(string='Name', help='Name of the custom receipts')
    design_receipt = fields.Text(string='Receipt XML',
                                 help='Add your customised receipts for pos')
    street_name = fields.Char(string='Street Name', help='Street name to display on POS receipts')
    city_name = fields.Char(string='City Name', help='City name to display on POS receipts')
