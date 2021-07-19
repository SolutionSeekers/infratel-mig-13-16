from . import models

from odoo import api, SUPERUSER_ID


def pre_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})
    _save_partner_info(env)


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    _get_partner_info(env)


def _save_partner_info(env):
    env.cr.execute("""
            CREATE TABLE partner_email AS SELECT id, email FROM res_partner WHERE email is not NULL;
        """)
    env.cr.execute("""
            CREATE TABLE user_signature AS SELECT id, signature FROM res_users;
        """)

def _get_partner_info(env):
    env.cr.execute("""
                SELECT * FROM partner_email;
            """)
    partner_info_list = env.cr.dictfetchall()
    for partner_dict in partner_info_list:
        partner = env['res.partner'].browse(partner_dict.get('id'))
        for company in env['res.company'].search([]):
            partner.with_context(company_id=company.id, force_company=company.id).write({'email': partner_dict.get('email')})

    env.cr.execute("""
                    SELECT * FROM user_signature;
                """)
    user_signature_list = env.cr.dictfetchall()
    for user_signature in user_signature_list:
        user = env['res.users'].browse(user_signature.get('id'))
        for company in env['res.company'].search([]):
            user.with_context(company_id=company.id, force_company=company.id).write({'signature_text': user_signature.get('signature')})

    env.cr.execute("""
            Drop TABLE partner_email;
        """)
    env.cr.execute("""
            Drop TABLE user_signature ;
        """)

