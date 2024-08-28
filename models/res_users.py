from odoo import fields, models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='salesman',
                                   domain=['|', ('state', '=', 'new'), ('state', '=', 'received')])
