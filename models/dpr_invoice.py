import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DamagedPropertyInvoice(models.Model):
    _name = 'dpr.invoice'
    _description = 'Invoice'
    _rec_name = 'dpr_position_id'

    dpr_position_id = fields.Many2one(
        comodel_name='dpr.position',
        string='Position',
    )

    unit_measurement = fields.Selection(
        selection=[
        ('m_sq', 'м.кв'),
        ('piece', 'шт.'),
        ],
    )

    price = fields.Float(
        compute='_compute_price_unit_measurement',
        readonly=True,
        store=True,
    )

    quantity = fields.Float(

    )

    company_id = fields.Many2one(
        comodel_name='res.company',
        readonly=True,
        default=lambda self: self.env.company,
    )

    company_currency_id = fields.Many2one(
        comodel_name="res.currency",
        string='Currency',
        related='company_id.currency_id',
        readonly=True,
        tracking=True,
    )

    total_sum = fields.Monetary(
        compute='_compute_total_sum',
        string='Sum',
        currency_field='company_currency_id',
        tracking=True,
        store=True,
    )

    dpr_application_id = fields.Many2one(
        comodel_name='dpr.application',
    )

    @api.depends('dpr_position_id')
    def _compute_price_unit_measurement(self):
        for record in self:
            if record.dpr_position_id:
                record.price = record.dpr_position_id.price
                record.unit_measurement = (record.dpr_position_id
                                           .unit_measurement)
            else:
                record.price = False
                record.unit_measurement = False

    @api.depends('quantity')
    def _compute_total_sum (self):
        for record in self:
            record.total_sum = record.price * record.quantity

