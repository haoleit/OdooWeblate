from odoo import http
from odoo.http import request

class WebsiteFeedbackController(http.Controller):

    @http.route('/feedback/submit', type='http', auth='public', website=True, methods=['POST'],csrf=False)
    def submit_feedback(self, **post):
        description = post.get('description', '').strip()
        if description:
            request.env['website.user.feedback'].sudo().create({
                'description': description,
            })
            return request.redirect('/feedback/thanks')
        return request.redirect('/feedback')

    @http.route('/feedback/thanks', type='http', auth='public', website=True)
    def feedback_thanks(self, **kwargs):
        return request.render('estate.feedback_thanks_template')
