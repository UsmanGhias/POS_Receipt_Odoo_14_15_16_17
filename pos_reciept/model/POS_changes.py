from odoo import api, models, fields

class POSConfig(models.Model):
    _inherit = 'pos.config'

    is_custom_header_footer = fields.Boolean(string='Custom Header & Footer', default=True)
    custom_header = fields.Text(string='Custom Header')
    custom_footer = fields.Text(string='Custom Footer')

    
    
