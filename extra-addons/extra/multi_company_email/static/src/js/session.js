odoo.define('multi_company_email.Session', function (require) {
    "use strict";

    var session = require('web.session');
    var SwitchCompanyMenu = require('web.SwitchCompanyMenu');

    SwitchCompanyMenu.include({
        _onSwitchCompanyClick: function (ev) {
            var dropdownItem = $(ev.currentTarget).parent();
            var companyID = dropdownItem.data('company-id');

            this._super.apply(this, arguments);
            this._rpc({
                model: 'res.users',
                args: [session.uid, companyID],
                method: 'compute_user_signature',
            });
        },
        _onToggleCompanyClick: function (ev) {
            if (ev.type == 'keydown' && ev.which != $.ui.keyCode.ENTER && ev.which != $.ui.keyCode.SPACE) {
                return;
            }

            this._super.apply(this, arguments);
            var allowed_company_ids = this.allowed_company_ids;
            var current_company_id = allowed_company_ids[0];
            this._rpc({
                model: 'res.users',
                args: [session.uid, current_company_id],
                method: 'compute_user_signature',
            });
        },
    });

});