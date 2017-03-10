# -*- coding: utf-8 -*-

import re

from odoo import api, fields, models
from odoo.osv import expression


class FundProject(models.Model):
    _description = 'Project and Fund relation'
    _name = 'cowin.fund.project.rel'
    _order = 'create_date desc'
    fund_id = fields.Many2one('cowin.fund', string=u"基金编号")
    project_id = fields.Many2one('cowin.project', string=u"项目名称")
    amount = fields.Float(string=u'金额')
