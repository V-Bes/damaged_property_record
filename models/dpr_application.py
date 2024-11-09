import logging

from bokeh.core.property import readonly

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DamagedPropertyApplication(models.Model):
    _name = 'dpr.application'
    _description = 'Application'
    _rec_name = 'drrp'

    drrp = fields.Integer(
        required=True,
        string='DRRP',
    )

    text_application = fields.Text(
        required=True,
    )

    approved = fields.Boolean(
        default=False
    )

    status_application = fields.Selection(
        selection=[
            ('new', 'new'),
            ('at_work', 'at work'),
            ('processed', 'processed'),
        ],
        compute='_compute_status_application',
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
    )

    position_ids = fields.One2many(
        comodel_name='dpr.position',
        inverse_name='dpr_application_id',
    )

    @api.depends('approved')
    def _compute_information_property_owner(self):
        if self.drrp and self.approved:
            domain_dpr = [('drrp', '=', self.drrp)]
            self.dpr_information_notice_id = (
                self.env['dpr.information.notice'].search(domain_dpr))
            if not self.dpr_information_notice_id:
                raise ValidationError(_('No information notice '
                                        'with this drrp code.'))
            else:
                self.dpr_property_id = (
                    self.dpr_information_notice_id.dpr_property_id)
                if not self.dpr_property_id:
                    raise ValidationError(_('No property '
                                            'with this information notice.'))
                else:
                    self.dpr_owner_id = self.dpr_property_id.dpr_owner_id
                    if not self.dpr_property_id:
                        raise ValidationError(_('No owner with '
                                                'this information notice.'))
        else:
            self.dpr_information_notice_id = False
            self.dpr_property_id = False
            self.dpr_owner_id = False

    @api.depends('approved')
    def _compute_status_application(self):
        for record in self:
            if record.approved:
                record.status_application = 'at_work'
            else:
                record.status_application = 'new'

    @api.onchange('approved')
    def _onchange_approved(self):
        if self.approved:
            if not (self.drrp and self.text_application):
                raise ValidationError(_('The application cannot approved, fill in '
                                    'the fields (DRRP and Text Application).'))
