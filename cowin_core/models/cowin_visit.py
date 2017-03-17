# -*- coding: utf-8 -*-

import re

from odoo import api, fields, models
from odoo.osv import expression


class Company(models.Model):
    _description = 'Visit'
    _name = 'cowin.visit'
    _order = 'create_date desc'

    company_id = fields.Many2one('res.partner', string=u"项目公司名称")
    project_ids=fields.One2many('cowin.project','company_id')
    manager_id = fields.Many2one("res.partner", string=u"项目经理")

    phone = fields.Char(related='company_id.phone', string=u"电话")
    email = fields.Char(related='company_id.email', string=u"邮箱")
    fax = fields.Char(related='company_id.fax', string=u"传真")

    company_background = fields.Char(string=u'公司背景')
    productsAndresearch = fields.Char(string=u'产品及研发')
    manager_team = fields.Char(string=u'管理团队')
    structure_needs = fields.Char(string=u'股权架构及融资需求')
    pre_judement = fields.Char(string=u'初步判断')
