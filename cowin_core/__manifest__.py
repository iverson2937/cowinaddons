# -*- coding: utf-8 -*-
{
    'name': "cowin_core",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Link Loving",
    'website': "http://www.linkloving.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/fund.xml',
        'views/project.xml',
        'views/company.xml',
        'views/visit.xml',
        'views/applicant.xml',
        'views/search_visit.xml',
        'views/invest_decision_applicant.xml',
        'views/invest_decision_committee_summary.xml',
        'data/fund_sequence_data.xml',
        'data/project_sequence_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}