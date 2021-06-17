# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class DevModel(models.Model):
    _inherit = "dev.model"

    @api.onchange(
        "model_type_id",
    )
    def onchange_partner_id(self):
        _super = super(DevModel, self)
        _super.onchange_partner_id()
        if self.model_type_id.default_partner != True:
            self.partner_id = False
