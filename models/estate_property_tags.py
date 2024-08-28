from odoo import fields, models, api


class PropertyTags(models.Model):
    _name = 'estate.property.tags'
    _description = 'Property tags'

    name = fields.Char(required=True)
