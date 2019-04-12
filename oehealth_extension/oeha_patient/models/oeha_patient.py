from odoo import api, fields, models, _
from odoo.exceptions import ValidationError,UserError
from datetime import timedelta,datetime

class OeHealthPatientExtension(models.Model):
    _inherit = 'oeh.medical.patient'
    _description = "Patient Extension"
    
    # inherited fields    
    phone = fields.Char(string="Phone", required=True)

    # additional fields
    next_of_kin = fields.Char(string="Next of kin")
    next_of_kin_contact = fields.Char(string="Next of kin contact number")
    children = fields.Many2many('res.partner', string="Children", domain="[('is_patient', '=', True)]",)

    @api.constrains('dob')
    def check_date_of_birth(self):
        for patient in self:
            dob = datetime.strptime(patient.dob.strftime("%Y-%m-%d"),'%Y-%m-%d')
            if dob > datetime.now():
                raise UserError("Date of birth cannot be in the future")

    # counts all evaluations belonging to patient
    @api.multi
    def _evaluation_count(self):
        oe_evaluation = self.env['oeh.medical.evaluation']
        for adm in self:
            domain = [('patient', '=', adm.id)]
            evaluation_ids = oe_evaluation.search(domain)
            evaluations = oe_evaluation.browse(evaluation_ids)
            evaluations_count = 0
            for ad in evaluations:
                evaluations_count+=1
            adm.evaluation_count = evaluations_count
        return True

    evaluation_count = fields.Integer(compute=_evaluation_count, string="Evaluations")




    


