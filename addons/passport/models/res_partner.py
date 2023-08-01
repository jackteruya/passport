from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Partner(models.Model):
    _inherit = ['res.partner']

    passport_number = fields.Char(string='Passport Number', index=True)
    issuance_date = fields.Date('Issuance Date')
    expiration_date = fields.Date('Expiration Date')

    @api.constrains('passport_number', 'issuance_date', 'expiration_date')
    def validate_passport(self):
        for record in self:
            self._validate_passport_number_required_dates(
                record.passport_number, record.issuance_date, record.expiration_date
            )
            self._validate_passport_date(record.issuance_date, record.expiration_date)

    @staticmethod
    def _validate_passport_number_required_dates(passport_number, issuance_date, expiration_date):
        if passport_number and (issuance_date is False or expiration_date is False):
            raise ValidationError("The issue date and expiration date are required.")

    @staticmethod
    def _validate_passport_date(issuance_date, expiration_date):
        if issuance_date > expiration_date:
            raise ValidationError("The issue date cannot be later than the expiration date.")
