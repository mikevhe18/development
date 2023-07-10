# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Development Model for Tester",
    "summary": "Development Model for Tester",
    "version": "14.0.1.0.0",
    "category": "Tools",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
        "ssi_master_data_mixin",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_cancel_mixin",
        "ssi_transaction_open_mixin",
        "ssi_custom_information_mixin",
        "ssi_status_check_mixin",
        "ssi_state_change_constrain_mixin",
        "ssi_related_attachment_mixin",
        "ssi_qr_code_mixin",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/dev_model_type_data.xml",
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "data/approval_template_data.xml",
        "data/policy_template_data.xml",
        "menu.xml",
        "views/dev_model_view.xml",
        "views/dev_model_type_view.xml",
        "views/dev_model_detail_view.xml",
    ],
}
