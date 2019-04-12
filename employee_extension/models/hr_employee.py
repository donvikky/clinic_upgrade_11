from odoo import api,fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Enhancements to the Employee Module'

    employee_identification_code = fields.Char(string="Employee ID", help="Employee ID")

    @api.model
    def create(self, vals):
        sequence = self.env['ir.sequence'].next_by_code('hr.employee')
        vals['employee_identification_code'] = sequence
        employee = super(HrEmployee, self).create(vals)
        return employee