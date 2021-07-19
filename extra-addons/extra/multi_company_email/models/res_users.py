from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)


class Users(models.Model):
    _inherit = "res.users"

    signature_text = fields.Text(company_dependent=True)
    signature = fields.Html(compute=False, store=True)

    def compute_user_signature(self, company_id=False):
        company = company_id or self.env.company.id
        for record in self:
            record.with_context(avoid_write=True).signature = record.with_context(force_company=company).signature_text

    @api.model_create_multi
    def create(self, vals_list):
        users = super(Users, self).create(vals_list)
        for user in users:
            if user.signature:
                user.signature_text = user.signature
        return users

    def update_signature_text(self, signature):
        self.signature_text = signature

    def write(self, vals):
        for record in self:
            if vals.get('signature') and not self.env.context.get('avoid_write'):
                record.update_signature_text(vals.get('signature'))
        return super(Users, self).write(vals)
