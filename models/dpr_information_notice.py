import logging
from datetime import timedelta


from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DamagedPropertyInformationNotice(models.Model):
    '''
    This model contains information notification data that
    is entered based on data from the owner
    '''
    _name = 'dpr.information.notice'
    _description = 'Information notice'
    _rec_name = 'number'
    _inherit = ['mail.thread', 'dpr.property']

    number = fields.Char(
        required=True,
    )

    drrp = fields.Char(
        required=True,
        string='DRRP',
    )

    description_damaged = fields.Text(
        required=True,
    )

    date_damaged = fields.Date(
        required=True,
    )

    date_create = fields.Date(
        default=fields.Datetime.now(),
        required=True,
    )

    date_end = fields.Date(
        default=fields.Datetime.now() + timedelta(days=14),
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

    @api.constrains('approved')
    @api.depends('approved')
    def _compute_property(self):
        '''
        This function populates the fields of a given model with property data.
        '''
        if self.drrp and self.approved:
            domain_property = [('drrp', '=', self.drrp)]
            self.dpr_property_id = (self.env['dpr.property'].
                                    search(domain_property))
            self.house_area = self.dpr_property_id.house_area
            self.number_storeys = self.dpr_property_id.number_storeys
            self.city = self.dpr_property_id.city
            self.address = self.dpr_property_id.address
            self.basement = self.dpr_property_id.basement
            self.attic = self.dpr_property_id.attic
            self.count_registered_people = (self.dpr_property_id.
                                            count_registered_people)
            if not self.dpr_property_id:
                raise ValidationError(_('No property with this drrp code.'))
        else:
            self.dpr_property_id = False
            self.house_area = False
            self.number_storeys = False
            self.city = False
            self.address = False
            self.basement = False
            self.attic = False
            self.count_registered_people = False

    @api.constrains('date_create')
    @api.depends('date_create')
    def _compute_date_end(self):
        '''
        This function sets the end date value.
        '''
        if self.date_create:
            self.date_end = self.date_create + timedelta(days=14)
        else:
            self.date_end = False
