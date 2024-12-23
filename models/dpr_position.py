import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DamagedPropertyPosition(models.Model):
    '''
    This model contains damaged property items
    '''
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

    invoice_ids = fields.One2many(
        comodel_name='dpr.invoice',
        inverse_name='dpr_position_id',
    )

    description = fields.Text()

    @api.constrains('name', 'unit_measurement', 'price')
    def _check_duplicate(self):
        '''
        This function checks that the phone number is entered correctly
        '''
        for record in self:
            is_duplicate = self.search([
                ('name', '=',
                 record.name),
                ('unit_measurement', '=',
                 record.unit_measurement),
                ('price', '=', record.price),
                ('id', '!=', record.id),
            ])
            if is_duplicate:
                raise ValidationError(_('Duplicate position found for the same'
                                        'name, unit measurement, and price.'))
