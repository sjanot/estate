from odoo import fields, models, api
from dateutil.relativedelta import relativedelta


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

