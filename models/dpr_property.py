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
    )

    address = fields.Text(
        required=True,
    )

    information_notice_ids = fields.One2many(
        comodel_name='dpr.information.notice',
        inverse_name='dpr_property_id',
    )
