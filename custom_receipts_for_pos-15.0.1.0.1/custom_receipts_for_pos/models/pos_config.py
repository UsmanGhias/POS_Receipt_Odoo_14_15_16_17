from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    """add field in pos config to select custom receipts"""

    receipt_design_id = fields.Many2one('pos.receipt', string="Receipt Design",
                                        help="Choose any receipt design")
    design_receipt = fields.Text(related='receipt_design_id.design_receipt',
                                 string='Receipt XML',
                                 help="Helps to get related receipt design")
    is_custom_receipt = fields.Boolean(string='Is Custom Receipt',
                                       help="Boolean field to enable the "
                                            "custom receipt design")
