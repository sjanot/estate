from odoo import fields, models, api
from dateutil.relativedelta import relativedelta


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate property offer'
    _sql_constraints = [
        ('price_check', 'check (price >= 0)', 'An offer price must be strictly positive!'),
    ]

    price = fields.Float(string='Price')
    status = fields.Selection(string='Status', selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one(comodel_name='res.partner', required=True)
    property_id = fields.Many2one(comodel_name='estate.property', required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_compute_date_deadline')

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date and record.validity:
                record.date_deadline = record.create_date.date() + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days=7)


    def accept_offer(self):
        for record in self:
            record.property_id.selling_price = record.price
            offers = self.env[self._name].search([('property_id', '=', record.property_id.id),
                                                               ('id', '!=', record.id)])
            for offer in offers:
                offer.status = 'refused'
            record.status = 'accepted'
        return True

    def refuse_offer(self):
        for record in self:
            record.status = 'refused'
        return True
