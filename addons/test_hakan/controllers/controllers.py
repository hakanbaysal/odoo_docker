# -*- coding: utf-8 -*-
from odoo import http

class TestHakan(http.Controller):
     @http.route('/test_hakan/test_hakan/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/test_hakan/test_hakan/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('test_hakan.listing', {
             'root': '/test_hakan/test_hakan',
             'objects': http.request.env['test_hakan.test_hakan'].search([]),
         })

     @http.route('/test_hakan/test_hakan/objects/<model("test_hakan.test_hakan"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('test_hakan.object', {
             'object': obj
         })