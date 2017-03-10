# -*- coding: utf-8 -*-

import re

from odoo import api, fields, models
from odoo.osv import expression


class Project(models.Model):
    _description = 'Project'
    _name = 'cowin.project'
    _order = 'name'

    name = fields.Char(required=True, string=u"项目登记号")
    full_name = fields.Char(string=u"项目名称")
    company_id = fields.Many2one('res.partner', string=u"选择被投企业")
    capital = fields.Float(string=u'预注册资本')
    apply_date=fields.Date(string=u"申请日期")
    manager_id=fields.Many2one("res.partner",string=u"投资经理")
    department_id=fields.Many2one('hr.department',string=u'所属部门')
    fund_type=fields.Selection([
        ("1","类型1"),
        ("1", "类型2")
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
