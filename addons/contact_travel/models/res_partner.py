from odoo import models, fields, api, _
import logging as log
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    voyage_ids = fields.One2many('voyage', 'partner_id', string='Voyages')

    voyage_count = fields.Integer( string='Voyages', compute='_compute_voyage_count')

  



    """
    Cette fonction permet d'afficher la liste des voyages liés au contact lorsqu'on clique sur le bouton intelligent
    """
    def schedule_voyage(self):
         return {
                    'name': 'Voyage',
                    'domain':[("partner_id", "=", self.id)],
                    'view_mode': 'tree,form',
                    'res_model': 'voyage',
                    'type': 'ir.actions.act_window',
                }



    """
    fonction pour calculer le total des voyages effectués par un utilisateur
    """
    def _compute_voyage_count(self):
       for partner in self:
            partner.voyage_count = len(partner.voyage_ids)


    
   