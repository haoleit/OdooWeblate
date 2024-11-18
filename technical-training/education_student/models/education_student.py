from odoo import models, fields

class EducationStudent(models.Model):
    _name = 'education.student'
    _description = 'Student Model'

    name = fields.Char(string="Student Name", required=True)
    image_1024 = fields.Binary(string="Image", attachment=True)
    responsible_id = fields.Many2one('res.users', string="Responsible")