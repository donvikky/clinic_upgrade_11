from odoo import api, fields, models, _
from odoo.exceptions import UserError
import datetime
from datetime import timedelta
import logging
import pytz

class OeHealthAppointment(models.Model):    
    _inherit = 'oeh.medical.appointment'
    _description = 'Extension to oehealth Appointment module'

    PATIENT_STATUS = [
        ('Ambulatory', 'Ambulatory'),
        ('Outpatient', 'Outpatient'),
        ('Inpatient', 'Inpatient'),
    ]

    APPOINTMENT_STATUS = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Invoiced', 'Invoiced'),
        ('In Progress', 'In Progress'),
    ]

    # Re-calculating Appointment End date by adding minutes to the start date
    @api.multi
    def _get_appointment_end(self):
        for apm in self:
            end_date = False
            duration = 1
            if apm.duration:
                duration = apm.duration
            if apm.appointment_date:
                end_date = datetime.datetime.strptime(apm.appointment_date, "%Y-%m-%d %H:%M:%S") + timedelta(minutes=duration)
            apm.appointment_end = end_date
        return True

    patient_status = fields.Selection(PATIENT_STATUS, string='Patient Status', readonly=True, states={'Scheduled': [('readonly', False)]}, default=lambda *a: 'Outpatient')
    state = fields.Selection(APPOINTMENT_STATUS, string='State', readonly=True, default=lambda *a: 'Scheduled')

    # redeclare duration field, Duration needs to be changed to minutes
    duration = fields.Integer(string='Duration (Minutes)', readonly=True, states={'Scheduled': [('readonly', False)]})
    appointment_end = fields.Datetime(compute=_get_appointment_end, string='Appointment End Date', readonly=True, states={'Scheduled': [('readonly', False)]})

    @api.multi
    def create_ticket(self):
        ticket_obj = self.env['helpdesk.ticket']
        team_id = self.env['ir.model.data'].get_object_reference('oehealth_extension','helpdesk_team_front_desk')
        ticket = {                    
                    'partner_id': self.patient.partner_id.id,
                    'appointment_id': self.id,
                    'team_id': team_id[1],
                    'name': self.name + " " + self.patient.name
                }
        ticket_id = ticket_obj.create(ticket)
        action = self.env.ref('helpdesk.helpdesk_ticket_action_main_tree').read()[0]
        action['views'] = [(self.env.ref('helpdesk.helpdesk_ticket_view_form').id, 'form')]
        action['res_id'] = ticket_id.id
        self.write({'state': 'In Progress'})
        return action

    