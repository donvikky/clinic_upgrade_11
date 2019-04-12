from odoo import api, fields, models, _


class OeHealthPrescriptionLineExtension(models.Model):
    _inherit = 'oeh.medical.prescription.line'
    _description='Extensions to Medical Prescription Line'

    dose = fields.Float(string='Dose', help="Amount of medicines (eg, 250 mg ) each time the patient takes it")    

    