from odoo import fields, models, api


class PropertyTypes(models.Model):
    _name = 'estate.property.types'
    _description = 'Estate property types'
    _order = "name asc"

    name = fields.Char(string='Name', required=True)
    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='property_type_id')
