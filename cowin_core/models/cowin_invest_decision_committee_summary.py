# -*- coding: utf-8 -*-

import re

from odoo import api, fields, models
from odoo.osv import expression


class Committee_Summary(models.Model):
    _description = 'invest decision committee summary'
    _name = 'cowin.committee_summary'
    _order = 'name'

    project_id = fields.Many2one('cowin.project', string=u'项目名称')
    company_id = fields.Many2one('res.partner', related='project_id.company_id', string=u"项目公司名称")
    manager_id = fields.Many2one("res.partner", related='project_id.manager_id', string=u"项目经理")
    name = fields.Char(string=u"项目编号", related='project_id.code_name')
    check_date = fields.Date(string=u'评审时间')
    invest_decision_committee_member = fields.Char(string=u"投资决策委员")

    committee_summary = fields.Text(string=u'会议纪要')
    partner_check_opinion = fields.Text(string=u'项目合伙人审核意见')
    reviewer = fields.Char(string=u'审核人')