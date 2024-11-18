import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    '''
    This model Extends the model res.partner
    '''
    _inherit = "res.partner"

    is_contact_dpr = fields.Boolean()
