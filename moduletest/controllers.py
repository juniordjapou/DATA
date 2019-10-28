# -*- coding: utf-8 -*-
from openerp import http

# class Moduletest(http.Controller):
#     @http.route('/moduletest/moduletest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/moduletest/moduletest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('moduletest.listing', {
#             'root': '/moduletest/moduletest',
#             'objects': http.request.env['moduletest.moduletest'].search([]),
#         })

#     @http.route('/moduletest/moduletest/objects/<model("moduletest.moduletest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('moduletest.object', {
#             'object': obj
#         })