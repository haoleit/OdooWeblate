# models/ir_ui_view_extension.py
from odoo import models, fields

class StudentView(models.Model):
    _inherit = 'ir.ui.view'

    type = fields.Selection(selection_add=[('student', 'Student')])
    

class ActWindowView(models.Model):
    _inherit = 'ir.actions.act_window.view'

    view_mode = fields.Selection(
        selection_add=[('student', 'Student')],
        ondelete={'student': 'cascade'}
    )
