# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging as log


"""   
"""
class Voyage(models.Model):

    _name = 'voyage'
    _description = 'Modèle des voyages' 

    name = fields.Char(string="Nom",required=True)
    date_of_departure = fields.Date(string='Departure Date')
    destination = fields.Char(string='Destination')
    partner_id = fields.Many2one('res.partner', string='Contact',required=True)
    montant = fields.Float(string="Prix en DA",required=True)