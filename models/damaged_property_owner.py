import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DamagedPropertyOwner(models.Model):
    _name = 'damaged.property.owner'
    _description = 'Owner'
    _rec_name = 'last_name'

    name = fields.Char()
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
        required=True,
    )

    foto = fields.Image(
        max_width=512,
        max_height=512,
    )

    birthday = fields.Date(
        required=True,
    )

    age = fields.Integer(
        compute='_compute_age'
    )

    passport = fields.Text(
        required=True,
    )

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for owner in self:
            owner.name = '%s_%s' % (
                    owner.first_name, owner.last_name)

    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                record.age = fields.Date.today().year - record.birthday.year
            else:
                record.age = 0