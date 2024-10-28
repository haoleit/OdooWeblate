from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _rec_name = "name"

    name = fields.Char(
        string="Name", 
        required=True, 
        unique=True
    )

    _sql_constraints = [
        ('name_unique', 'UNIQUE(LOWER(name))', 'The property type name must be unique')
    ]

    @api.constrains('name')
    def _check_name_unique(self):
        for record in self:
            existing = self.search([('name', '=ilike', record.name)], limit=1)
            if existing and existing.id != record.id:
                raise ValidationError("The property type name must be unique")
