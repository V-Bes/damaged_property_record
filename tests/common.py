from odoo import fields
from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()

        self.test_application1 = self.env['dpr.application'].create({
            'number': 'Test',
            'drrp': 0,
            'text_application': 'Test_1',
            'date_creation': fields.Datetime.now(),
        })

        self.dpr_position1 = self.env['dpr.position'].create({
            'name': 'Test',
            'unit_measurement': 'm_sq',
            'price': 12.5,
        })

        self.test_position1 = self.env['dpr.position'].create({
            'name': 'Test',
            'unit_measurement': 'm_sq',
            'price': 12,
        })
