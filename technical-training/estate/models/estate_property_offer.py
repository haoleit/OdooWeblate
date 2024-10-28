from datetime import timedelta
from odoo import api, fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    price = fields.Float(
        string="Price", 
        required=True
    )
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        string="Status", 
        copy=False
    )
    partner_id = fields.Many2one(
        'res.partner', 
        string="Partner", 
        required=True
    )
    property_id = fields.Many2one(
        'estate.property', 
        string="Property", 
        required=True
    )
    property_type_id = fields.Many2one(
        related="property_id.property_type_id"
    )
    validity = fields.Integer(
        string="Validity (days)", 
        default=7
    )
    date_deadline = fields.Date(
        string="Deadline", 
        compute="_compute_date_deadline", 
        store=True
    )
    
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)

  
    
