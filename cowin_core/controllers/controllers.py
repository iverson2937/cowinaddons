# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CowinCore(http.Controller):
    @http.route("/index/index", type="http", auth="public", csrf=False)
    def index(self, **kw):
        print kw

#
#     @http.route('/cowin_core/cowin_core/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cowin_core.listing', {
#             'root': '/cowin_core/cowin_core',
#             'objects': http.request.env['cowin_core.cowin_core'].search([]),
#         })

#     @http.route('/cowin_core/cowin_core/objects/<model("cowin_core.cowin_core"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cowin_core.object', {
#             'object': obj
#         })