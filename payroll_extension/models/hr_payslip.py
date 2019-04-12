#
# Extensions to Odoo 11 payroll module

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HrPayslip(models.Model):
    _inherit = 'hr.payslip'
    _description = 'Pay Slip Extension'

    worked_days_in_month = fields.Integer(string="Days worked", help="Number of days worked in month", default="21")

    @api.constrains('worked_days_in_month')
    def _check_worked_days(self):
        '''
        checks if the worked_days_in_month variable is a digit between 1 and 31
        '''
        for record in self:
            worked_days = record.worked_days_in_month

            if worked_days < 1 or worked_days > 31:
                raise ValidationError('Number of days worked must be a number between 1 and 31')



