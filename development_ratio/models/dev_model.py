# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import api, fields, models
from openerp.addons.decimal_precision import decimal_precision as dp


class DevModel(models.Model):
    _inherit = "dev.model"

    ratio = fields.Float(
        string="Ratio",
        digits_compute=dp.get_precision("Account"),
    )

    @api.onchange(
        "model_type_id",
        "ratio",
    )
    def onchange_value(self):
        _super = super(DevModel, self)
        _super.onchange_value()
        if self.ratio > 0.0:
            self.value = self.value * self.ratio
