from odoo import http
from odoo.http import request

class WebsiteForm(http.Controller):

    @http.route('/get_states', type='json', auth='public')
    def get_states(self, country_id):
        states = request.env['res.country.state'].search([('country_id', '=', country_id)])
        return [{'id': state.id, 'name': state.name} for state in states]
    
    @http.route('/form_page', type='http', auth='public', website=True)
    def form_page(self, **kwargs):
        return http.request.render('oao_select_city.website_form_page')
