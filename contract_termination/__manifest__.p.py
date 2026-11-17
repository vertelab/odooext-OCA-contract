# Copyright 2025 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Contract Termination",
    "summary": """contract_termination""",
    "version": "1.0.2",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/contract",
    "depends": ["contract_line_successor"],
    "data": [
        "security/groups.xml",
        # #if VERSION >= "20.0"
        "security/ir.access.csv",
        # #else
        "security/ir.model.access.csv",
        # #endif
        "security/contract_terminate_reason.xml",
        "views/contract_contract.xml",
        "views/contract_terminate_reason.xml",
        "wizards/contract_contract_terminate.xml",
    ],
    "demo": [],
}
