
from odoo import api, fields, models, _

class OeHealthInsuranceOrganisation(models.Model):
    _name = 'oeha.insurance.organisation'
    _description = "Insurance Companies"

    _inherits={
        'res.partner': 'partner_id',
    }

    partner_id = fields.Many2one('res.partner', string='Related Partner', required=True, ondelete='cascade', help='Partner-related data of the insurance company')
    
    _defaults={
        'is_insurance_company': True,
    }

    @api.model
    def create(self, vals):
        vals["is_insurance_company"] = True
        insurance = super(OeHealthInsuranceOrganisation, self).create(vals)
        return insurance


# re-declare insurance class and override completely
class OeHealthInsurance(models.Model):
    _name = 'oeh.medical.insurance'
    _description = "Insurances"    

    STATE = [
        ('Draft','Draft'),
        ('Active','Active'),
        ('Expired','Expired'),
    ]

    name = fields.Char(string="Insurance ID", compute='_get_id')
    insurance_company = fields.Many2one('oeha.insurance.organisation', string="HMO", required=True)
    ins_no = fields.Char(string='Insurance #', size=64, required=True)
    patient = fields.Many2one('oeh.medical.patient', string='Patient', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    exp_date = fields.Date(string='Expiration date', required=True)
    ins_type = fields.Many2one('oeh.medical.insurance.type', string='Insurance Type', required=True)
    info = fields.Text(string='Extra Info')
    state = fields.Selection(STATE, string='State', readonly=True, copy=False, help="Status of insurance", default=lambda *a: 'Draft')

    @api.depends('insurance_company','ins_no')
    def _get_id(self):
        for record in self:
            if record.ins_no and record.insurance_company:
                record.name =  record.insurance_company.name + " [" + record.ins_no + ']'

    @api.multi    
    def name_get(self):
        res = []
        for record in self:            
            name = "[" + record.ins_no + '] ' + record.insurance_company.name
            res += [(record.id, name)]
        return res

    @api.multi
    def make_active(self):
        self.write({'state': 'Active'})
        return True




    

    