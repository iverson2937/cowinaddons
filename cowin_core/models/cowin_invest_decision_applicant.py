# -*- coding: utf-8 -*-

import re

from odoo import api, fields, models
from odoo.osv import expression


class Invest_Applicant(models.Model):
    _description = 'invest decision applicant'
    _name = 'cowin.invest_applicant'
    _order = 'name'

    project_id = fields.Many2one('cowin.project', string=u'项目名称')
    company_id = fields.Many2one('res.partner', related='project_id.company_id', string=u"项目公司")
    manager_id = fields.Many2one("res.partner", related='project_id.manager_id', string=u"项目经理")
    name = fields.Char(string=u"项目编号",related='project_id.code_name')
    search_check_date = fields.Date(string=u'尽职调查审核日期')
    submit_data_manifest = fields.Binary(string=u'提交资料清单')
    partner_pre_check_opinion = fields.Text(string=u'项目合伙人预审意见')
    reviewer = fields.Char(string=u'审核人')
    risk_reveal = fields.Text(string=u'风险揭示')
    risk_control_director = fields.Char(string=u'风险控制总监')
    invest_decision_committee_date = fields.Date(string=u'投资决策委员会召开时间')