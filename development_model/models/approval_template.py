# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class ApprovalTemplate(models.Model):
    _inherit = "approval.template"

    @api.model
    def _get_multiple_approval_model_names(self):
        res = super(ApprovalTemplate, self)._get_multiple_approval_model_names()
        res.append("dev.model")
        return res
