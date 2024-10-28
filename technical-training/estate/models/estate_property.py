from odoo import api, fields, models
from datetime import timedelta

from odoo.exceptions import ValidationError


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Post Code")
    date_availability = fields.Date(
        string="Date Availability", 
        copy=False, 
        default=lambda self: fields.Date.today() + timedelta(days=90)
    )
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True, copy=False)
    bed_room = fields.Integer(string="Bed Room", default=2)
    living_area = fields.Integer(string="Living Area")
    farcades = fields.Integer(string="Farcades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string ="Garden Area")
    garden_orientation = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ('east', "East"),
            ("west", "West")
        ],
        string="Garden Orientation"
    )
    active = fields.Boolean(
        string="Active", 
        default=True
    )
    state = fields.Selection(
        [
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')
        ],
        string="State",
        required=True,
        copy=False,
        default='new'
        
    )
    property_type_id = fields.Many2one(
        "estate.property.type", 
        string="Property Type", 
        ondelete="set null"
    )
    salesperson_id = fields.Many2one(
        'res.users', 
        string="Salesperson", 
        default=lambda self: self.env.user
    )
    buyer_id = fields.Many2one(
        'res.partner', 
        string="Buyer", 
        copy=False
    )
    offer_ids = fields.One2many(
        'estate.property.offer', 
        'property_id', 
        string="Offers"
    )
    tag_ids = fields.Many2many(
        'estate.property.tag',         
        'estate_property_tag_rel',      
        'property_id',                  
        'tag_id',                       
        string="Tags"
    )
    total_area = fields.Integer(
        string="Total Area",
        compute="_compute_total_area",
        store=True
    )
    best_price=fields.Float(
        string="Best Price",
        compute="_compute_best_price",
        store=True
    )

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = (record.living_area or 0) + (record.garden_area or 0)

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped('price'))
            else:
                record.best_price = 0
                
    @api.onchange('garden')
    def onchange_garden(self):
        if self.garden:
            self.garden_area=50
            self.garden_orientation='north'
        else:
            self.garden_area=0
            self.garden_orientation=False

    @api.constrains('date_availability')
    def _check_date_availability(self):
        for record in self:
            if record.date_availability and record.date_availability < fields.Date.today():
                raise ValidationError("Date Availability cannot be set to a date prior to today.")