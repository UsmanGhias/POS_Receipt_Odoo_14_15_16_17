from odoo import fields, models


class PosReceipt(models.Model):
    """New model for create POS receipt designs."""
    _name = 'pos.receipt'
    _description = 'POS Receipt'

    name = fields.Char(string='Name', help="Provide a name for record")
    design_receipt = fields.Text(string='Receipt XML',
                                 help='Add your customised receipt design '
                                      'for POS')
