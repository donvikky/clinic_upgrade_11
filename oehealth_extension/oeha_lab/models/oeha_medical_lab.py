
from odoo import api, fields, models, _
import time
import datetime
import qrcode
import base64
from io import StringIO, BytesIO
from datetime import datetime


class OeHealthLabTestsExtension(models.Model):
    _inherit = 'oeh.medical.lab.test'
    _description = 'Lab Tests Extension'

    lab_department = fields.Many2one('oeh.medical.labtest.department', string='Department', required=False)
    test_type = fields.Many2one('oeh.medical.labtest.types', string='Test Type', required=True, readonly=True, states={'Draft': [('readonly', False)]}, help="Lab test type")
    qr_image = fields.Binary('QR Code')
    formatted_time = fields.Char(string="Formatted creation time", compute='_compute_creation_time')

    #add new field for the patient ID
    identification_code = fields.Char(string="Patient ID", related="patient.identification_code")

    @api.model
    def create(self, vals):
        # generate a qr_code of the sample name and save to the database

        lab_test = super(OeHealthLabTestsExtension, self).create(vals)

        qr = qrcode.QRCode(version=1, box_size=10, border=2)
        qr.add_data(lab_test.name)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="white", back_color="black")
        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        qrcode_str = base64.b64encode(buffer.getvalue())
        lab_test.write({'qr_image': qrcode_str})
        return lab_test

    @api.depends('create_date')
    def _compute_creation_time(self):
        """ This function creates a user friendly version of the time a test was created """
        for test in self:
            unformatted_time = datetime.strptime(test.create_date, '%Y-%m-%d %H:%M:%S')
            test.formatted_time = datetime.strftime(unformatted_time, "%d %b %Y")
