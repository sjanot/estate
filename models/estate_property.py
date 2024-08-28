from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


class Property(models.Model):
    _name = 'estate.property'
    _description = 'Property'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(copy=False, default=lambda self: fields.Date.today() + relativedelta(months=3),
                                    string='Available From')
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(readonly=True, copy=False, string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([('north', 'North'),
                                           ('south', 'South'),
                                           ('east', 'East'),
                                           ('west', 'West')])
    active = fields.Boolean(default=True)
    state = fields.Selection([('new', 'New'),
                              ('received', 'Offer Received'),
                              ('accepted', 'Offer Accepted'),
                              ('sold', 'Sold'),
                              ('canceled', 'Canceled')], default='new', copy=False)
    property_type_id = fields.Many2one(comodel_name='estate.property.types')
    buyer = fields.Many2one(comodel_name='res.partner', copy=False)
    salesman = fields.Many2one(comodel_name='res.users', default=lambda self: self.env.user)
    tag_ids = fields.Many2many(comodel_name='estate.property.tags', string="Property Tags")
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_id')
    total_area = fields.Integer(compute='_compute_total_area', string='Total Area (sqm)')
    best_price = fields.Float(compute='_compute_best_price', string='Best offer')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0

    @api.onchange("garden")
    def _onchange_garden(self):
        for record in self:
            if record.garden:
                record.garden_area = 10
                record.garden_orientation = 'north'
            else:
                record.garden_area = False
                record.garden_orientation = False

    def cancel_property(self):
        for record in self:
            if record.state == 'sold':
                raise UserError('A sold property cannot be set as canceled!')
            record.state = "canceled"
        return True

    def sold_property(self):
        for record in self:
            if record.state == 'sold':
                raise UserError('A canceled property cannot be set as sold!')
            record.state = "sold"
        return True