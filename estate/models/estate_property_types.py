from odoo import fields, models, api


class PropertyTypes(models.Model):
    _name = 'estate.property.types'
    _description = 'Estate property types'
    _order = "name asc"

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence', default=1)
    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='property_type_id')
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_type_id')
    offer_count = fields.Integer(compute='_compute_offer_count')


    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
        return True

