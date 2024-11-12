import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class DprFillOutChecklist(models.TransientModel):
    _name = 'dpr.fill.out.checklist.wizard'
    _description = 'Fill out checklist.'

    position_ids = fields.Many2many(
        comodel_name='dpr.position',
    )

    def get_sum(self):
        sum = 0
        for record in self.position_ids:
            sum = sum + record.price
        return sum

    def calculate_amount(self):
        active_ids = self.env.context.get('active_ids')
        for record in active_ids:
            application_id = self.env['dpr.application'].browse(record)
            application_id.position_ids = self.position_ids
            application_id.total_amount = self.get_sum()

