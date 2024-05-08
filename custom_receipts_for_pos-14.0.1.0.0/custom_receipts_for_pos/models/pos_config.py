from odoo import fields, models


class PosConfig(models.Model):
    """Add new fields in pos.config for enable the option and then select
    any design."""
    _inherit = "pos.config"

    receipt_design_id = fields.Many2one('pos.receipt', string="Receipt Design",
                                        help="Choose any receipt design",
                                        required=True)
    design_receipt = fields.Text(related='receipt_design_id.design_receipt',
                                 string='Receipt XML',
                                 help="Write xml code for generate new receipt "
                                      "design")
    is_custom_receipt = fields.Boolean(string='Custom Receipt',
                                       help="Enable option for use customised "
                                            "design.")
