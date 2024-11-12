import logging
from datetime import timedelta

from odoo.exceptions import ValidationError
from .common import TestCommon
from odoo import fields

_logger = logging.getLogger(__name__)


class TestHospital(TestCommon):

    def test_01_action_owner_duplicate(self):
        with self.assertRaises(ValidationError):
            self.test_owner2 = self.env['dpr.owner'].create({
                'first_name': self.test_owner1.first_name,
                'last_name': self.test_owner1.last_name,
                'phone': self.test_owner1.phone,
            })

    def test_02_action_application_approved(self):
        with self.assertRaises(ValidationError):
            self.test_application1.write({
                'approved': 'True',
                })

    def test_03_action_application_approved(self):
        with self.assertRaises(ValidationError):
            self.test_property1 = self.env['dpr.property'].create({
                'house_area': 25,
                'year_construction': fields.Datetime.now() + timedelta(days=1),
                'registration_date_BTI': fields.Datetime.now(),
                'count_registered_people': 3,
                'drrp': 545,
                'address': 'Test',
                'number_storeys': 12,
            })