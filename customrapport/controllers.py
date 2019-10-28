# -*- coding: utf-8 -*-
from openerp import http

# class Customrapport(http.Controller):
#     @http.route('/customrapport/customrapport/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customrapport/customrapport/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customrapport.listing', {
#             'root': '/customrapport/customrapport',
#             'objects': http.request.env['customrapport.customrapport'].search([]),
#         })

#     @http.route('/customrapport/customrapport/objects/<model("customrapport.customrapport"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customrapport.object', {
#             'object': obj
#         })