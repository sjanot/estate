from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _inherit = 'estate.property'

    def sold_property(self):
        self.ensure_one()
        if not self.buyer:
            raise ValidationError("Buyer must be set before selling the property.")
        new_account = self.env['account.move'].create({
            'partner_id': self.buyer.id,
            'move_type': 'out_invoice',
            'journal_id': 1
        })

        print("Sold property inherited")

        # Call the parent method to continue the standard process
        return super().sold_property()

