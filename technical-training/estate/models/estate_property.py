from odoo import api,fields,models

class EstateProperty(models.Model):
    _name="estate.property"
    _description="Estate Property"

    name=fields.Char(string="Name",required=True)
    description=fields.Text(string="Description")
    postcode=fields.Char(string="Post Code")
    date_availability=fields.Date(string="Date Availability")
    expected_price=fields.Float(string="Expected Price",required=True)
    selling_price=fields.Float(string="Selling Price")
    bed_room=fields.Integer(string="Bed Room")
    living_area=fields.Integer(string="Living Area")
    farcades=fields.Integer(string="Farcades")
    garage=fields.Boolean(string="Garage")
    garden=fields.Boolean(string="Garden")
    garden_area=fields.Integer(string="Garden Area")
    garden_orientation=fields.Selection([("north","North"),("south","South"),('east',"East"),("west","West")],string="Garden Orientation")
    
  
    