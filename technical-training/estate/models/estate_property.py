from odoo import api, fields, models
from datetime import timedelta


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
    active = fields.Boolean(string="Active", default=True)
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
