# -*- coding: utf-8 -*-

import re

from odoo import api, fields, models
from odoo.osv import expression


class Project(models.Model):
    _description = 'Project'
    _name = 'cowin.project'
    _order = 'name'

    code_name = fields.Char(string=u"项目编号")
    name = fields.Char(string=u"项目名称")
    company_id = fields.Many2one('res.partner', string=u"选择被投企业")

    phone=fields.Char(related='company_id.phone',string=u"电话")
    email=fields.Char(related='company_id.email',string=u"邮箱")
    fax=fields.Char(related='company_id.fax',string=u"传真")

    capital = fields.Float(string=u'预注册资本')
    apply_date=fields.Date(string=u"申请日期")
    manager_id=fields.Many2one("res.partner",string=u"项目经理")
    department_id=fields.Many2one('hr.department',string=u'所属部门')
    fund_type=fields.Selection([
        ("1","类型1"),
        ("2", "类型2")
    ],string=u"项目类型")
    partner_id = fields.Many2one('res.partner',string=u"信息登记者")
    source=fields.Selection([
        ("1",u"企业自荐"),
        ("2", u"朋友介绍"),
    ],string=u"项目来源")
    state = fields.Selection([
        ("draft", "Draft"),
        ("done", "Done")
    ], string=u"所处阶段")

    @api.model
    def create(self,vals):
        if not vals.get('code_name'):
            vals['code_name'] = self.env['ir.sequence'].next_by_code('cowin.project') or '/'
        return super(Project, self).create(vals)

