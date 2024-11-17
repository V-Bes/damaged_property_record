import logging

from bokeh.core.property import readonly

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DamagedPropertyApplication(models.Model):
    _name = 'dpr.application'
    _description = 'Application'
    _rec_name = 'drrp'
    _inherit = ['mail.thread']

    number = fields.Char(
        required=True,
    )

    drrp = fields.Char(
        string='DRRP',
    )

    type_application = fields.Selection(
        selection=[
            ('type_application_1', 'Заява на отримання компенсації за пошкоджене майно'),
            ('type_application_2', 'Заява на виїзд комісії з візуального обстеження'),
            ('type_application_3', 'Заява на отримання акту обстеження пошкодженого майна'),
        ],
    )

    approved = fields.Boolean(
        default=False
    )

    date_creation = fields.Date(
        required=True,
    )

    status_application = fields.Selection(
        selection=[
            ('new', 'new'),
            ('at_work', 'at work'),
            ('processed', 'processed'),
        ],
        string='Status',
        default='new',
        readonly='True',
    )

    dpr_property_id = fields.Many2one(
        comodel_name='dpr.property',
        string="Property",
        readonly="True",
    )

    dpr_owner_id = fields.Many2one(
        comodel_name='dpr.owner',
        string="Owner",
        readonly="True",
    )

    dpr_information_notice_id = fields.Many2one(
        compute='_compute_information_property_owner',
        comodel_name='dpr.information.notice',
        string="Information notice",
        readonly="True",
        store=True
    )

    invoice_ids = fields.One2many(
        comodel_name='dpr.invoice',
        inverse_name='dpr_application_id',
    )

    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True,
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

    total_amount = fields.Monetary(
        string='Total amount',
        currency_field='company_currency_id',
        readonly=True,
        tracking=True,
    )

    @api.depends('approved','total_amount')
    def _compute_information_property_owner(self):
        for record in self:
            if record.drrp and record.approved:
                domain_dpr = [('drrp', '=', record.drrp),
                              ('approved', '=', True)]
                record.dpr_information_notice_id = (
                    record.env['dpr.information.notice'].search(domain_dpr))
                if not record.dpr_information_notice_id:
                    raise ValidationError(_('No information notice '
                                            'with this drrp code.'))
                else:
                    record.dpr_property_id = (
                        record.dpr_information_notice_id.dpr_property_id)
                    if not record.dpr_property_id:
                        raise ValidationError(_('No property '
                                                'with this information notice.'))
                    else:
                        record.dpr_owner_id = record.dpr_property_id.dpr_owner_id
                        if not record.dpr_property_id:
                            raise ValidationError(_('No owner with '
                                                    'this information notice.'))
            else:
                record.dpr_information_notice_id = False
                record.dpr_property_id = False
                record.dpr_owner_id = False
                record.invoice_ids = False
                record.total_amount = False

    @api.constrains('approved','total_amount')
    @api.depends('approved','total_amount')
    def _compute_status_application(self):
        for record in self:
            if record.approved and record.total_amount:
                record.status_application = 'processed'
            elif record.approved:
                record.status_application = 'at_work'
            else:
                record.status_application = 'new'

    @api.onchange('approved')
    @api.constrains('approved')
    def _onchange_approved(self):
        if self.approved:
            if not (self.drrp and self.type_application):
                raise ValidationError(_('The application cannot approved, fill in '
                                    'the fields (DRRP and Type Application).'))

    @api.onchange('invoice_ids')
    @api.constrains('invoice_ids')
    def _compute_sum(self):
        self.total_amount = 0
        for record in self.invoice_ids:
            self.total_amount = self.total_amount + record.total_sum
