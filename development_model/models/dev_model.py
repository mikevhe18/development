# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import api, fields, models
from openerp.addons.decimal_precision import decimal_precision as dp


class DevModel(models.Model):
    _name = "dev.model"
    _description = "Development Model"
    _inherit = [
        "tier.validation",
        "base.sequence_document",
        "base.workflow_policy_object",
        "base.cancel.reason_common",
        "base.terminate.reason_common",
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
        default="/",
        required=True,
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
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
    value = fields.Float(
        string="Value",
        digits_compute=dp.get_precision("Account"),
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

    @api.onchange(
        "model_type_id",
    )
    def onchange_partner_id(self):
        self.partner_id = False
        if self.model_type_id:
            self.partner_id = self.model_type_id.partner_id

    @api.onchange(
        "model_type_id",
    )
    def onchange_value(self):
        self.value = 0.0
        if self.model_type_id:
            self.value = self.model_type_id.value

    @api.model
    def create(self, values):
        _super = super(DevModel, self)
        result = _super.create(values)
        sequence = result._create_sequence()
        result.write({
            "name": sequence,
        })
        return result

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

    def validate_tier(self):
        _super = super(DevModel, self)
        _super.validate_tier()
        for document in self:
            if document.validated:
                document.action_open()
