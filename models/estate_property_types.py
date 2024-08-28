from odoo import fields, models, api


class PropertyTypes(models.Model):
    _name = 'estate.property.types'
    _description = 'Estate property types'

    name = fields.Char(string='Name', required=True)
