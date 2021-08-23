from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import UserError


class Partners(models.Model):
    _inherit = 'res.partner'

    email = fields.Char(company_dependent=True)
    company_dependent_email = fields.Char(company_dependent=True)
    name = fields.Char(store= True, company_dependent=True)

    @api.model_create_multi
    def create(self, vals_list):
        partners = super(Partners, self).create(vals_list)
        for partner in partners.filtered(lambda p: p.email):
            email = partner.email
            name = partner.name
            for company_id in self.env['res.company'].search([]):
                partner.with_context(force_company=company_id.id).email = email
                partner.with_context(force_company=company_id.id).name = name
        return partners

    def write(self, vals):
        if 'email' in vals or 'name' in vals and not self.env.context.get('force_partner_email'):
            for partner in self.filtered(lambda p: not p.user_ids):
                for company_id in self.env['res.company'].search([]):
                    partner.with_context(force_company=company_id.id, force_partner_email=True).email = vals.get('email')
                    partner.with_context(force_company=company_id.id, force_partner_email=True).name = vals.get('name')
        return super(Partners, self).write(vals)

