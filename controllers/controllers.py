# -*- coding: utf-8 -*-
# from odoo import http


# class Fct(http.Controller):
#     @http.route('/fct/fct', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fct/fct/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fct.listing', {
#             'root': '/fct/fct',
#             'objects': http.request.env['fct.fct'].search([]),
#         })

#     @http.route('/fct/fct/objects/<model("fct.fct"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fct.object', {
#             'object': obj
#         })
