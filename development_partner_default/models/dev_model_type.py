# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class DevModelType(models.Model):
    _inherit = "dev.model.type"

    default_partner = fields.Boolean(
        string="Set Partner as Default",
        default=True,
    )
