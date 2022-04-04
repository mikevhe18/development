# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class DevModelType(models.Model):
    _name = "dev.model.type"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Development Model Type"
    _field_name_string = "Type"

    value = fields.Integer(
        string="Value",
    )
