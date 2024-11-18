import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class DamagedPropertyCity(models.Model):
    '''
    This model contains cities.
    '''
    _name = 'dpr.city'
    _description = 'City'
    _rec_name = 'name'

    name = fields.Char(
        required=True,
    )

    @api.constrains('name')
    def _check_duplicate(self):
        '''
        This function checks for duplicates.
        '''
        for record in self:
            is_duplicate = self.search([
                ('name', '=',
                 record.name),
                ('id', '!=', record.id),
            ])
            if is_duplicate:
                raise ValidationError(_('Duplicate name found for the same'
                                        'name.'))
