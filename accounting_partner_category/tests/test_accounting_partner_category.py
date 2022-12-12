from psycopg2.errors import UniqueViolation

from odoo.tests.common import TransactionCase


class AccountingPartnerCategory(TransactionCase):
    def test_tag_unique(self):
        self.env["accounting.partner.category"].create({"name": "test"})
        with self.assertRaisesRegex(
            UniqueViolation, "accounting_partner_category_name_uniq"
        ):
            self.env["accounting.partner.category"].create({"name": "test"})
