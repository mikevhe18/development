# Copyright 2018 Eficent Business and IT Consulting Services S.L.
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class DevModel(models.Model):
    _name = "dev.model"
    _description = "Development Model"
    _inherit = [
        "tier.validation.mixin",
        "mail.thread",
    ]
    _state_from = [
        "draft",
        "confirm"
    ]
    _state_to = [
        "open",
    ]

    name = fields.Char(
        string="# Document",
        required=True,
    )
    active = fields.Boolean(
        string="Active",
        default=True,
    )
    notes = fields.Text(
        string="Notes",
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("open", "On Progress"),
            ("done", "Finished"),
            ("cancel", "Cancelled"),
        ],
        default="draft",
    )

    def action_confirm(self):
        for document in self:
            document.write({"state": "confirm"})
            document.request_validation()

    def action_open(self):
        for document in self:
            document.write({"state": "open"})

    def action_done(self):
        for document in self:
            document.write({"state": "done"})

    def action_cancel(self):
        for document in self:
            document.write({"state": "cancel"})
            document.restart_validation()

    def validate_tier(self):
        _super = super(DevModel, self)
        _super.validate_tier()
        for document in self:
            if document.validated:
                document.action_open()