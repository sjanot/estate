from odoo import fields, models, api
from dateutil.relativedelta import relativedelta

from odoo.exceptions import UserError


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate property offer'
    _sql_constraints = [
        ('price_check', 'check (price >= 0)', 'An offer price must be strictly positive!'),
    ]
    _order = "price desc"

    price = fields.Float(string='Price')
    status = fields.Selection(string='Status', selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
    partner_id = fields.Many2one(comodel_name='res.partner', required=True)
    property_id = fields.Many2one(comodel_name='estate.property', required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_compute_date_deadline')
    property_type_id = fields.Many2one(related='property_id.property_type_id', stored=True)

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

    @api.model
    def create(self, vals):
        property_record = self.env['estate.property'].browse(vals['property_id'])

        property_record.state = 'received'
        if property_record.best_price > vals['price']:
            raise UserError('You cannot create offer with lower price %(best_price)s!' % {'best_price':
                                                                                            property_record.best_price})
        return super().create(vals)
