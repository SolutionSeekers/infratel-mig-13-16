from odoo import api, fields, models

ADDRESS_FIELDS = ('street', 'street2', 'zip', 'city', 'state_id', 'country_id', 'l10n_mx_edi_colony')

class ResPartners(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _get_address_format(self):
        if self.country_id.code == 'MX':
            return "%(street)s %(street2)s\n%(l10n_mx_edi_colony)s\n%(zip)s %(city)s, %(state_code)s\n%(country_name)s"
        else:
            return self.country_id.address_format or self._get_default_address_format()


    @api.model
    def _address_fields(self):
        """Returns the list of address fields that are synced from the parent."""
        return list(ADDRESS_FIELDS)