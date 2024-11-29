
from odoo import api, models, fields

class DemoWidget(models.Model):
    _name = 'demo.widget'
    _description = 'Demo Widget'
    

    name = fields.Char(string="Name")
    color = fields.Integer(string="Color")  
    from_date = fields.Date(string="From Date") 
    to_date = fields.Date(string="To Date") 


   
