# Copyright 2018 Eficent Business and IT Consulting Services S.L.
# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class DevModel(models.Model):
    _name = "dev.model"
    _description = "Development Model"
    _inherit = [
        "mixin.transaction_confirm",
        "mixin.transaction_cancel",
        "mixin.transaction_open",
        "mixin.transaction_done",
    ]
    _approval_from_state = "draft"
    _approval_to_state = "open"
    _approval_state = "confirm"
    _after_approved_method = "action_open"
    _create_sequence_state = "open"

    @api.model
    def _get_policy_field(self):
        res = super(DevModel, self)._get_policy_field()
        policy_field = [
            "confirm_ok",
            "approve_ok",
            "open_ok",
            "done_ok",
            "cancel_ok",
            "reject_ok",
            "restart_ok",
            "restart_approval_ok",
            "manual_number_ok",
        ]
        res += policy_field
        return res

    @api.depends("policy_template_id")
    def _compute_policy(self):
        _super = super(DevModel, self)
        _super._compute_policy()

    name = fields.Char(
        string="# Document",
        default="/",
        copy=False,
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    model_type_id = fields.Many2one(
        string="Type",
        comodel_name="dev.model.type",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    date = fields.Date(
        string='Date',
        index=True,
        readonly=True,
        states={'draft': [('readonly', False)]},
        copy=False,
        default=fields.Date.context_today
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("open", "On Progress"),
            ("done", "Finished"),
            ("cancel", "Cancelled"),
            ("reject", "Rejected"),
        ],
        default="draft",
    )

    @api.onchange(
        "model_type_id",
    )
    def onchange_policy_template_id(self):
        if self.model_type_id:
            template_id = self._get_template_policy()
            self.policy_template_id = template_id

    def action_approve_approval(self):
        _super = super(DevModel, self)
        _super.action_approve_approval()
        for document in self:
            if document.approved:
                document.action_open()
