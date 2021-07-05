FROM llacox/odoo:13.0
MAINTAINER Aztlan Munoz <amr@indboo.com>

COPY --chown=odoo ./extra-addons /var/lib/extra-addons
COPY ./odoo.conf /etc/odoo/

