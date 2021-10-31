# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Development Model for Tester",
    "summary": "Development Model for Tester",
    "version": "11.0.1.0.0",
    "category": "Tools",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "mail",
        "ssi_multiple_approval_mixin",
    ],
    "data": [
        "security/ir.model.access.csv",
        "menu.xml",
        "views/dev_model_view.xml",
        "views/dev_model_type_view.xml",
    ],
}
