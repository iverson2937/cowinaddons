# -*- coding: utf-8 -*-

import re

from odoo import api, fields, models
from odoo.osv import expression


class Search(models.Model):
    _description = 'search'
    _name = 'cowin.search'
    _order = 'create_date desc'

    project_id = fields.Many2one('cowin.project', string=u'项目名称')
    company_id = fields.Many2one('res.partner', related='project_id.company_id', string=u"项目公司")
    manager_id = fields.Many2one("res.partner", related='project_id.manager_id', string=u"项目经理")
    searchs_types = fields.Selection([
        ("team","团队"),
        ("customer", "客户"),
        ("provider", "供应商"),
        ("competitor", "竞争对手"),
    ],string=u"调研类型")
    name = fields.Char(string=u"公司名称")
    visit_date = fields.Date(string=u"拜访时间")
    contacter = fields.Char(string=u"联系人")
    contacter_position = fields.Char(string=u"职务")
    tel = fields.Char(string=u"电话")
    email = fields.Char(string=u"邮箱")

    relationship_with_plan_invest = fields.Text(string=u"与拟投资项目关系")
    positive_evaluation_to_plan_invest = fields.Text(string=u"对拟投资项目正面评价")
    negative_evaluation_to_plan_invest = fields.Text(string=u"对拟投资项目负面评价")
    other_issues = fields.Text(string=u"其他关键问题/意见")
    other_could_search_visit = fields.Text(string=u"其他可以跟进拜访对象")