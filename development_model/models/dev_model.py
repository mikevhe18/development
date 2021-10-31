# Copyright 2018 Eficent Business and IT Consulting Services S.L.
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class DevModel(models.Model):
    _name = "dev.model"
    _description = "Development Model"
    _inherit = [
        "mixin.multiple_approval",
        "mail.thread",
    ]
    _approval_state_from = [
        "draft",
        "confirm"
    ]
    _approval_state_to = [
        "open",
    ]

    name = fields.Char(
        string="# Document",
        default="/",
        required=True,
    )
    model_type_id = fields.Many2one(
        string="Type",
        comodel_name="dev.model.type",
    )
    date = fields.Date(
        string='Date',
        index=True,
        readonly=True,
        states={'draft': [('readonly', False)]},
        copy=False,
        default=fields.Date.context_today
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
            ("terminate", "Terminated"),
        ],
        default="draft",
    )

    def action_confirm(self):
        for document in self:
            document.write({"state": "confirm"})
            document.action_request_approval()

    def action_open(self):
        for document in self:
            document.write({"state": "open"})

    def action_done(self):
        for document in self:
            document.write({"state": "done"})

    def action_cancel(self):
        for document in self:
            document.write({"state": "cancel"})

    def action_restart(self):
        for document in self:
            document.write({"state": "draft"})

    def action_approve_approval(self):
        _super = super(DevModel, self)
        _super.action_approve_approval()
        for document in self:
            if document.approved:
                document.action_open()
