#
#
# Extensions for adding symptoms
######################################
from odoo import api, fields, models, _


class OeHealthSymptomCategory(models.Model):
    _description='Symptom Category'
    _name = 'oeha.medical.symptom.category'

    name = fields.Char(string='Category', required=True, size=128)
    description = fields.Text(string='Description')


class OeHealthSymptom(models.Model):
    _description='Symptoms'
    _name = 'oeha.medical.symptom'

    name = fields.Char(string='Sympton name', required=True, size=128)
    category = fields.Many2one('oeha.medical.symptom.category', string='Category')
    description = fields.Text(string='Description')