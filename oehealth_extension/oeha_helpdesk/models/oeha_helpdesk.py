import datetime
from datetime import timedelta
import logging
import pytz
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo.tools.translate import _
# from builtins import True

_logger = logging.getLogger(__name__)

class HelpdeskTicket(models.Model):
    #_name = 'helpdesk.ticket'
    _description = 'Ticket'
    _inherit = ['helpdesk.ticket']
    
    @api.one
    @api.depends('partner_id')    
    def _get_patient(self):
        self.patient_id = None
        patient = self.env['oeh.medical.patient'].search([('partner_id','=',self.partner_id.id)])
        if patient:
            self.patient_id = patient.id    
    
    
    @api.multi
    def _app_count(self):
        oe_apps = self.env['oeh.medical.appointment']
        for pa in self:
            domain = [('patient', '=', pa.patient_id.id)]
            app_ids = oe_apps.search(domain)
            apps = oe_apps.browse(app_ids)
            app_count = 0
            for ap in apps:
                app_count+=1
            pa.app_count = app_count
        return True
    
    @api.multi
    def _eval_count(self):
        oe_apps = self.env['oeh.medical.evaluation']
        for pa in self:
            domain = [('patient', '=', pa.patient_id.id)]
            app_ids = oe_apps.search(domain)
            apps = oe_apps.browse(app_ids)
            app_count = 0
            for ap in apps:
                app_count+=1
            pa.eval_count = app_count
        return True
    
    @api.multi
    def _prescription_count(self):
        oe_pres = self.env['oeh.medical.prescription']
        for pa in self:
            domain = [('patient', '=', pa.patient_id.id)]
            pres_ids = oe_pres.search(domain)
            pres = oe_pres.browse(pres_ids)
            pres_count = 0
            for pr in pres:
                pres_count+=1
            pa.prescription_count = pres_count
        return True

    @api.multi
    def _admission_count(self):
        oe_admission = self.env['oeh.medical.inpatient']
        for adm in self:
            domain = [('patient', '=', adm.patient_id.id)]
            admission_ids = oe_admission.search(domain)
            admissions = oe_admission.browse(admission_ids)
            admission_count = 0
            for ad in admissions:
                admission_count+=1
            adm.admission_count = admission_count
        return True

    @api.multi
    def _vaccine_count(self):
        oe_vac = self.env['oeh.medical.vaccines']
        for va in self:
            domain = [('patient', '=', va.patient_id.id)]
            vec_ids = oe_vac.search(domain)
            vecs = oe_vac.browse(vec_ids)
            vecs_count = 0
            for vac in vecs:
                vecs_count+=1
            va.vaccine_count = vecs_count
        return True
    
    @api.multi
    def _labtest_count(self):
        oe_labs = self.env['oeh.medical.lab.test']
        for ls in self:
            domain = [('patient', '=', ls.patient_id.id)]
            lab_ids = oe_labs.search(domain)
            labs = oe_labs.browse(lab_ids)
            labs_count = 0
            for lab in labs:
                labs_count+=1
            ls.labs_count = labs_count
        return True

    # @api.multi
    # def _imagingtest_count(self):
    #     oe_images = self.env['oeha.medical.imaging.test']
    #     for ls in self:
    #         domain = [('patient', '=', ls.patient_id.id)]
    #         image_ids = oe_images.search(domain)
    #         images = oe_images.browse(image_ids)
    #         images_count = 0
    #         for image in images:
    #             images_count+=1
    #         ls.images_count = images_count
    #     return True

    @api.multi
    def _invoice_count(self):
        oe_invoice = self.env['account.invoice']
        for inv in self:
            invoice_ids = self.env['account.invoice'].search([('patient', '=', inv.patient_id.id)])
            invoices = oe_invoice.browse(invoice_ids)
            invoice_count = 0
            for inv_id in invoices:
                invoice_count+=1
            inv.invoice_count = invoice_count
        return True

    # Ticket assignment
    @api.multi
    def assign_to_front_desk_team(self, team):    
        self.ensure_one()        
        get_team_id = self.env['ir.model.data'].get_object_reference('oehealth_extension','helpdesk_team_front_desk')
        stage_id = self.env['helpdesk.stage'].search([('team_ids', 'in', get_team_id[1])], order='sequence', limit=1).id
        self.sudo().write({
            'team_id':get_team_id[1],
            'user_id':False,
            'stage_id':stage_id            
        })                

    @api.multi
    def assign_to_nurse_team(self, team):
        self.ensure_one()
        get_team_id = self.env['ir.model.data'].get_object_reference('oehealth_extension','helpdesk_team_nurse')
        stage_id = self.env['helpdesk.stage'].search([('team_ids', 'in', get_team_id[1])], order='sequence', limit=1).id        
        self.sudo().write({
            'team_id':get_team_id[1],
            'user_id':False,
            'stage_id':stage_id
        })                

    @api.multi
    def assign_to_doctor_team(self, team):
        self.ensure_one()
        get_team_id = self.env['ir.model.data'].get_object_reference('oehealth_extension','helpdesk_team_doctor')
        stage_id = self.env['helpdesk.stage'].search([('team_ids', 'in', get_team_id[1])], order='sequence', limit=1).id
        self.sudo().write({
            'team_id':get_team_id[1],
            'user_id':False,
            'stage_id':stage_id            
        })

    @api.multi
    def assign_to_pharmacy_team(self, team):
        self.ensure_one()
        get_team_id = self.env['ir.model.data'].get_object_reference('oehealth_extension','helpdesk_team_pharm')
        stage_id = self.env['helpdesk.stage'].search([('team_ids', 'in', get_team_id[1])], order='sequence', limit=1).id
        self.sudo().write({
            'team_id':get_team_id[1],
            'user_id':False,
            'stage_id':stage_id            
        })

    @api.multi
    def assign_to_lab_team(self, team):
        self.ensure_one()
        get_team_id = self.env['ir.model.data'].get_object_reference('oehealth_extension','helpdesk_team_lab')
        stage_id = self.env['helpdesk.stage'].search([('team_ids', 'in', get_team_id[1])], order='sequence', limit=1).id
        self.sudo().write({
            'team_id':get_team_id[1],
            'user_id':False,
            'stage_id':stage_id            
        })
    
    appointment_id = fields.Many2one('oeh.medical.appointment', string='Appointment', index=True, ondelete='cascade')
    patient_id = fields.Many2one('oeh.medical.patient', string='Patient', index=True, ondelete='cascade',compute='_get_patient', store=True)
    dob = fields.Date(string="Date of birth", related="patient_id.dob")
    phone = fields.Char(string="Phone", related="patient_id.phone")
    eval_count = fields.Integer(compute=_eval_count, string="Evaluations")
    prescription_count = fields.Integer(compute=_prescription_count, string="Prescriptions")
    admission_count = fields.Integer(compute=_admission_count, string="Admission / Discharge")
    vaccine_count = fields.Integer(compute=_vaccine_count, string="Vaccines")
    labs_count = fields.Integer(compute=_labtest_count, string="Lab Tests")
    #images_count = fields.Integer(compute=_imagingtest_count, string="Imaging Tests")
    app_count = fields.Integer(compute=_app_count, string="Appointments")
    invoice_count = fields.Integer(compute=_invoice_count, string="Invoices")
    payer_type = fields.Many2one(string="Payer Type", related="partner_id.property_product_pricelist")
