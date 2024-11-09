import logging

from bokeh.core.property import readonly

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DamagedPropertyInformationNotice(models.Model):
    _name = 'dpr.information.notice'
    _description = 'Information notice'
    _rec_name = 'drrp'

    drrp = fields.Integer(
        required=True,
        string='DRRP',
    )

    description_damaged = fields.Text(
        required=True,
    )

    date_damaged = fields.Date(
        required=True,
    )

    approved = fields.Boolean(
        default=False
    )

    dpr_property_id = fields.Many2one(
        compute='_compute_property',
        comodel_name='dpr.property',
        string="Property",
        readonly="True",
    )

    @api.depends('approved')
    def _compute_property(self):
        if self.drrp and self.approved==True:
            domain_property = [('drrp', '=', self.drrp)]
            self.dpr_property_id = (self.env['dpr.property']
                                .search(domain_property))
            if not self.dpr_property_id:
                raise ValidationError(_('No property with this drrp code.'))
        else:
            self.dpr_property_id = False
