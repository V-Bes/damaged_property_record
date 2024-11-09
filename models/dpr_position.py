import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DamagedPropertyPosition(models.Model):
    _name = 'dpr.position'
    _description = 'Position'
    _rec_name = 'name'

    name = fields.Char(
        required=True,
    )

    unit_measurement = fields.Selection(
        selection=[
        ('m_sq', 'м.кв'),
        ('piece', 'шт.'),
        ],
        required=True)

    price = fields.Float(
        required=True,
    )

    dpr_application_id = fields.Many2one(
        comodel_name='dpr.application',
    )

    description = fields.Text()
