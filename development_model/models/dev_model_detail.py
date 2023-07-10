# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class DevModelDetail(models.Model):
    _name = "dev.model_detail"
    _description = "Development Model Detail"

    dev_model_id = fields.Many2one(
        string="#Dev Model",
        comodel_name="dev.model"
    )
    description = fields.Char(
        string="Description",
    )
    amount = fields.Float(
        string="Amount",
    )
