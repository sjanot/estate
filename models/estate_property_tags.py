from odoo import fields, models, api


class PropertyTags(models.Model):
    _name = 'estate.property.tags'
    _description = 'Property tags'
    _sql_constraints = [
        ('unique_name', 'unique(name)', 'A property tag name and property type name must be unique!'),
    ]
    _order = "name asc"

    name = fields.Char(required=True)
    color = fields.Integer(string='Color')