from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()

        self.test_owner1 = self.env['dpr.owner'].create({
            'first_name': 'Test_patient1',
            'last_name': 'Test_patient1',
            'phone': '0631234567',
        })

        self.test_application1 = self.env['dpr.application'].create({
            'drrp': 0,
            'text_application': 'Test_1',
        })
