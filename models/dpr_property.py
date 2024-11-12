import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DamagedPropertyProperty(models.Model):
    _name = 'dpr.property'
    _description = 'Property'
    _rec_name = 'address'

    description = fields.Text()

    dpr_owner_id = fields.Many2one(
        comodel_name='dpr.owner',
        string="Owner",
    )

    house_area = fields.Integer(
        required=True,
    )

    year_construction = fields.Date(
        required=True,
    )

    number_storeys = fields.Integer(
        required=True,
    )

    registration_date_BTI = fields.Date(
        required=True,
    )

    basement = fields.Boolean(
        default=False,
    )

    attic = fields.Boolean(
        default=False,
    )

    count_registered_people = fields.Integer(
        required=True,
    )

    drrp = fields.Integer(
        required=True,
        string='DRRP',
    )

    address = fields.Text(
        required=True,
    )

    information_notice_ids = fields.One2many(
        comodel_name='dpr.information.notice',
        inverse_name='dpr_property_id',
    )

    @api.constrains('drrp')
    def _check_duplicate(self):
        for record in self:
            is_duplicate = self.search([
                ('drrp', '=', record.drrp),
                ('id', '!=', record.id),
            ])
            if is_duplicate:
                raise ValidationError(_('Duplicate property found for the same '
                                        'DRRP.'))

    @api.constrains('year_construction','registration_date_BTI')
    def _check_duplicate(self):
        for record in self:
            if record.year_construction > record.registration_date_BTI :
                raise ValidationError(_('The registration date cannot be '
                                        'greater than the construction date.'))