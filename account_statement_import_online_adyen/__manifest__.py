# Copyright 2021-2023 - Therp BV <https://therp.nl>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Online Bank Statements: Adyen payment report",
    "version": "16.0.1.0.0",
    "category": "Account",
    "website": "https://github.com/OCA/bank-statement-import",
    "author": "Ronald Portier (Therp BV), Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "account_statement_import_adyen",
        "account_statement_import_online",
    ],
    "data": ["views/online_bank_statement_provider.xml"],
}
