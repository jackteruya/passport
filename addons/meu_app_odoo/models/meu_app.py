import datetime

from odoo import api, fields, models


class MeuApp(models.Model):
    _name = 'meu_app'
    _description = 'Meu APP'

    name = fields.Char('Name')
    status = fields.Selection(
        string='Status',
        selection=[('done', 'Done'), ('processing', 'Processing'), ('pending', 'Pending')]
    )
    active = fields.Boolean('Active')
    date_done = fields.Datetime('Date Done')

    def action_do_something(self):
        for record in self:
            if record.status == 'processing':
                record.status = "done"
                record.date_done = datetime.datetime.utcnow()
        return True
#     _inherit = 'res.users'
#
#     passport = fields.Char(string='Passaport', default="Extended")
