# -*- coding: utf-8 -*-
from openerp import http

# class PosCashier(http.Controller):
#     @http.route('/pos_cashier/pos_cashier/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_cashier/pos_cashier/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_cashier.listing', {
#             'root': '/pos_cashier/pos_cashier',
#             'objects': http.request.env['pos_cashier.pos_cashier'].search([]),
#         })

#     @http.route('/pos_cashier/pos_cashier/objects/<model("pos_cashier.pos_cashier"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_cashier.object', {
#             'object': obj
#         })