import json 
import yaml
from odoo import http 
from odoo.http import Response, request


class BemoController(http.Controller):


    @http.route('/bemo', type='http', auth='public', website=True)
    def render_bemo(self, **kwargs):
        return request.render('estate.bemo_page')

    
   
    
   
   