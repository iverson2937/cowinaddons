# -*- coding: utf-8 -*-

import re

from odoo import api, fields, models
from odoo.osv import expression


class Preproject(models.Model):
    _description = "setup project"
    _name = "cowin.applicant"
    _order = "create_date desc"

    code_name = fields.Char(related='project_id.code_name',string=u"项目编号")
    project_id = fields.Many2one('cowin.project',string=u"项目名称")
    industry = fields.Char(string=u"所属行业")
    state = fields.Selection([
        ("draft", "Draft"),
        ("done", "Done")
    ], string=u"所处阶段",related='project_id.state')
    register_located = fields.Char(string=u"项目注册地")
    run_located = fields.Char(string=u"项目运营地区")
    project_source = fields.Char(string=u"项目来源")
    project_partner = fields.Char(string=u"项目合伙人")
    project_applicant = fields.Char(string=u"立项申请人")
    applicant_date = fields.Date(string=u"申请时间")

    company_introduction = fields.Html(string=u"公司介绍")
    project_basis = fields.Html(string=u"立项依据")

    opinion_project_partner = fields.Html(string=u"项目合伙人表决意见")
    opinion_risk_control = fields.Html(string=u"风险控制总监表决意见")
    opinion_manage_partner = fields.Html(string=u"管理合伙人表决意见")