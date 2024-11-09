import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class DprFillOutChecklist(models.TransientModel):
    _name = 'dpr.fill.out.checklist.wizard'
    _description = 'Fill out checklist.'

    position_ids = fields.Many2many(
        comodel_name='dpr.position',
    )

    def calculate_amount(self):
        active_ids = self.env.context.get('active_ids')
        for record in active_ids:
            patient_id = self.env['hr.hospital.patient'].browse(record)
            patient_id.hr_hospital_doctor_id = self.doctor_id
