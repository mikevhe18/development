# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class DevModel(models.Model):
    _name = "dev.model"
    _description = "Development Model"
    _inherit = [
        "mixin.transaction_confirm",
        "mixin.transaction_cancel",
        "mixin.transaction_open",
        "mixin.transaction_done",
        "mixin.custom_info",
        "mixin.status_check",
        "mixin.state_change_constrain",
        "mixin.related_attachment",
        "mixin.qr_code",
    ]
    _approval_from_state = "draft"
    _approval_to_state = "open"
    _approval_state = "confirm"
    _after_approved_method = "action_open"
    _create_sequence_state = "open"
    _related_attachment_create_page = True
    _qr_code_create_page = True

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
    number = fields.Char(
        string="Number",
        default="00000",
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
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
    )
    user_id = fields.Many2one(
        string="User",
        comodel_name="res.users",
    )
    date = fields.Date(
        string='Date',
        index=True,
        readonly=True,
        states={'draft': [('readonly', False)]},
        copy=False,
        default=fields.Date.context_today
    )
    date_time = fields.Datetime(
        string='Datetime',
        index=True,
        readonly=True,
        states={'draft': [('readonly', False)]},
        copy=False,
    )
    detail_ids = fields.One2many(
        string="Details",
        comodel_name="dev.model_detail",
        inverse_name="dev_model_id",
        ondelete="cascade",
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

    # @api.onchange(
    #     "model_type_id",
    # )
    # def onchange_policy_template_id(self):
    #     if self.model_type_id:
    #         template_id = self._get_template_policy()
    #         self.policy_template_id = template_id

    def action_approve_approval(self):
        _super = super(DevModel, self)
        _super.action_approve_approval()
        for document in self:
            if document.approved:
                document.action_open()

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if "date_time" in vals:
                vals["create_date"] = vals["date_time"]
        raise UserError(_("%s")%(vals_list))
        _super = super(DevModel, self)
        result = _super.create(vals_list)
        template_id = result._get_template_status_check()
        if template_id:
            result.write(
                {
                    "status_check_template_id": template_id,
                }
            )
            result.create_status_check_ids()
            result.onchange_state_change_constrain_template_id()
        return result
