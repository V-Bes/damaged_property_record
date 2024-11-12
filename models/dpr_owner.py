import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DamagedPropertyOwner(models.Model):
    _name = 'dpr.owner'
    _description = 'Owner'
    _rec_name = 'last_name'

    description = fields.Text()

    first_name = fields.Char(
        required=True,
    )

    last_name = fields.Char(
        required=True,
    )

    phone = fields.Char(
        required=True,
    )

    gender = fields.Selection(
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
        ],
    )

    foto = fields.Image(
        max_width=512,
        max_height=512,
    )

    birthday = fields.Date(

    )

    age = fields.Integer(
        compute='_compute_age'
    )

    passport = fields.Text(

    )

    property_ids = fields.One2many(
        comodel_name='dpr.property',
        inverse_name='dpr_owner_id',
        readonly="True",
    )

    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                record.age = fields.Date.today().year - record.birthday.year
            else:
                record.age = 0

    @api.constrains('first_name', 'last_name', 'phone')
    def _check_duplicate(self):
        for record in self:
            is_duplicate = self.search([
                ('first_name', '=',
                 record.first_name),
                ('last_name', '=',
                 record.last_name),
                ('phone', '=', record.phone),
                ('id', '!=', record.id),
            ])
            if is_duplicate:
                raise ValidationError(_('Duplicate owner found for the same '
                                        'first name, last name, and phone.'))
