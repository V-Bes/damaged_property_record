import logging
from datetime import timedelta

from odoo.exceptions import ValidationError
from odoo import fields
from .common import TestCommon

_logger = logging.getLogger(__name__)


class TestHospital(TestCommon):

    def test_01_action_owner_phone(self):
        with self.assertRaises(ValidationError):
            self.test_owner1 = self.env['dpr.owner'].create({
                'first_name': 'Test',
                'last_name': 'Test',
                'phone': '111',
                'birthday': fields.Datetime.now(),
                'passport': 'Test',
            })

    def test_02_action_application_approved(self):
        with self.assertRaises(ValidationError):
            self.test_application1.write({
                'approved': 'True',
                })

    def test_03_action_property_date(self):
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

    def test_04_action_information_notice_approved(self):
        with ((((self.assertRaises(ValidationError))))):
            self.test_information_notice1 = self.env[('dpr.information.'
                                                      'notice')].create(
                {
                    'number': 'Test',
                    'drrp': 111,
                    'description_damaged': 'Test',
                    'date_damaged': fields.Datetime.now(),
                    'approved': 'True',
                    'house_area': 15,
                    'number_storeys': 15,
                    'count_registered_people': 15,
                    'year_construction': fields.Datetime.now(),
                    'registration_date_BTI': fields.Datetime.now(),
                }
            )

    def test_05_action_position_duplicate(self):
        with self.assertRaises(ValidationError):
            self.test_position2 = self.env['dpr.position'].create({
                'name': self.test_position1.name,
                'unit_measurement': self.test_position1.unit_measurement,
                'price': self.test_position1.price,
            })
