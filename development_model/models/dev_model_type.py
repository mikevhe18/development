# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import api, fields, models
from openerp.addons.decimal_precision import decimal_precision as dp


class DevModelType(models.Model):
    _name = "dev.model.type"
    _description = "Development Model Type"

    name = fields.Char(
        string="# Document",
        required=True,
    )
    code = fields.Char(
        string="Code",
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
    )
    value = fields.Float(
        string="Value",
        digits_compute=dp.get_precision("Account"),
    )
    sequence_id = fields.Many2one(
        string="Sequence",
        comodel_name="ir.sequence",
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    notes = fields.Text(
        string="Notes",
    )
