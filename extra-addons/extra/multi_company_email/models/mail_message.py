# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import re

from odoo import _, api, fields, models, modules, tools
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

# TODO: ADJUST VALIDATION TO TAKE PORTAL AND PUBLIC USERS INTO CONSIDERATION
class Message(models.Model):
    _inherit = 'mail.message'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('subtype_id') == self.env.ref('mail.mt_comment').id and vals.get('model') and vals.get('res_id') and hasattr(self.env[vals.get('model')], 'company_id'):
                record_company_id = self.env[vals.get('model')].browse(vals.get('res_id')).company_id
                if self.env[vals.get('model')].browse(vals.get('res_id')).company_id and self.env.company != record_company_id:
                    raise ValidationError(_("This record is from {}, and you are trying to send an email from {}".format(record_company_id.name, self.env.company.name)))

        return super(Message, self).create(vals_list)
