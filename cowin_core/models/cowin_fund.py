# -*- coding: utf-8 -*-

import re

from odoo import api, fields, models
from odoo.osv import expression


class Fund(models.Model):
    _description = 'Fund'
    _name = 'cowin.fund'
    _order = 'name'

    name = fields.Char(string=u"基金编号")
    full_name = fields.Char(string=u"基金全称")
    company_id = fields.Many2one('res.partner', string=u"管理公司")
    capital = fields.Float(string=u'预注册资本')
    apply_date=fields.Date(string=u"申请日期")
    fund_type=fields.Selection([
        ("1","类型1"),
        ("1", "类型2")
    ])
    partner_id = fields.Many2one('res.partner',string=u"经办人")
    state = fields.Selection([
        ("draft", "Draft"),
        ("done", "Done")
    ], string=u"所处阶段")

    @api.model
    def create(self,vals):
        if not vals.get('name'):
            vals['name'] = self.env['ir.sequence'].next_by_code('cowin.fund') or '/'
            print vals['name']
        return super(Fund, self).create(vals)

