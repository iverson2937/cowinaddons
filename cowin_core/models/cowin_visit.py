# -*- coding: utf-8 -*-

import re

from odoo import api, fields, models
from odoo.osv import expression


class Visit(models.Model):
    _description = 'Visit'
    _name = 'cowin.visit'
    _order = 'create_date desc'

    project_id = fields.Many2one('cowin.project', string=u'项目名称')
    company_id = fields.Many2one('res.partner',related='project_id.company_id', string=u"项目公司名称")
    manager_id = fields.Many2one("res.partner",related='project_id.manager_id', string=u"项目经理")

    phone = fields.Char(related='company_id.phone', string=u"电话")
    email = fields.Char(related='company_id.email', string=u"邮箱")
    fax = fields.Char(related='company_id.fax', string=u"传真")
    address = fields.Char(related='company_id.street', string=u'地址')

    company_background = fields.Html(string=u'公司背景')
    products_And_research = fields.Html(string=u'产品及研发')
    manager_team = fields.Html(string=u'管理团队')
    structure_needs = fields.Html(string=u'股权架构及融资需求')
    pre_judgement = fields.Html(string=u'初步判断')