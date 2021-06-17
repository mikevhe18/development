# Copyright 2020 OpenSynergy Indonesia
# Copyright 2020 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Development Model for Tester",
    "summary": "Development Model for Tester",
    "version": "8.0.1.0.0",
    "category": "Tools",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base_multiple_approval",
        "base_sequence_configurator",
        "base_cancel_state",
        "base_terminate_state",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/base_sequence_configurator_data.xml",
        "data/base_cancel_reason_configurator_data.xml",
        "data/base_terminate_reason_configurator_data.xml",
        "menu.xml",
        "views/dev_model_view.xml",
        "views/dev_model_type_view.xml",
    ],
}
