import json 
import yaml
from odoo import http 
from odoo.http import Response, request


class EstateController(http.Controller):


    @http.route('/estates', type='http', auth='public', website=True)
    def list_estates(self, page=1, search='', **kwargs):
        try:
            Estate = request.env['estate.property']
            domain = [('name', 'ilike', search)] if search else []
            
            # Fetch estates with pagination
            estates = Estate.sudo().search(domain, offset=(int(page) - 1) * 12, limit=12)
            total = Estate.search_count(domain)

            return request.render('estate.estates_page', {
                'estates': estates,
                'search': search,
                'page': int(page),
                'total_pages': (total + 11) // 12,
            })
        except Exception as e:
            return request.not_found()

    
    @http.route('/estates/<int:estate_id>', type='http', auth='public', website=True)
    def estate_details(self,estate_id,**kwargs):
        # Fetch estate details by ID
        estate = request.env['estate.property'].browse(estate_id)
        return request.render('estate.estate_detail_page',{'estate':estate})
    
    
    @http.route("/api/estates", type='http', auth="public", methods=['GET'])
    def get_estates(self, **kwargs):
        estates = request.env['estate.property'].search([])
        data = [
            {
            'id': e.id, 
            'name': e.name, 
            'selling_price': e.selling_price,
            'date_availability': e.date_availability.isoformat() if e.date_availability else None } 
            for e in estates]
        return Response(json.dumps(data), content_type='application/json', status=200)

    @http.route("/api/estates", type='json', auth='public', methods=["POST"],csrf=False, cors="*")
    def create_estate(self,**kwargs):
        data = request.jsonrequest   
        try:
            estate = request.env['estate.property'].sudo().create(data)
            return Response(json.dumps({"estate_id": estate.id}), content_type='application/json', status=201)
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json', status=400)
   
    @http.route("/api/estates/<int:estate_id>", type="json", auth="public", methods=["PUT", "PATCH"])
    def update_estate(self, estate_id, **kwargs):
        data = request.jsonrequest
        estate = request.env['estate.property'].browse(estate_id)
        if not estate:
            return Response({'error': "Estate not found"}, content_type='application/json', status=404)
        try:
            estate.sudo().write(data)
            return Response({'status': "success"}, content_type='application/json', status=200)
        except Exception as e:
            return Response({'error': str(e)}, content_type='application/json', status=400)

    @http.route("/api/estates/<int:estate_id>", type="json", auth="public", methods=["DELETE"])
    def delete_estate(self, estate_id, **kwargs):
        estate = request.env['estate.property'].browse(estate_id)
        if not estate:
            return Response({'error': "Estate not found"}, content_type='application/json', status=404)
        try:
            estate.unlink()
            return Response({'status': 'success'}, content_type='application/json', status=200)
        except Exception as e:
            return Response({'error': str(e)}, content_type='application/json', status=400)

    # @http.route("/api/test", type="http", auth="public", methods=["GET"])
    # def test_controller(self, **kwargs):
    #     return Response(json.dumps({'status': 'success'}),content_type="application/json", status=200)