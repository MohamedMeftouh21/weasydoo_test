from odoo import models, fields, api, _
import logging as log


class ResPartner(models.Model):
    _inherit = 'res.partner'

    voyage_ids = fields.One2many('voyage', 'partner_id', string='Voyages')

    voyage_count = fields.Integer( string='Voyages', compute='_compute_voyage_count') #
    #depense_totale = fields.Float(string="Dépense Totale",compute="_compute_total_depense")#

    recompense_levels = fields.Selection(
    [('argent', 'Argent'), ('or', 'Or'), ('platine', 'Platine')],
    string='Niveau de récompense',
    default='argent',
    required=True,
    compute="_compute_recompense_levels" ,readonly=False,
    store=True

)

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






    """
    Cette fonction met à jour automatiquement le niveau de récompense du client,
    en fonction de ses dépenses de voyage.
    """
    @api.depends('recompense_levels','voyage_ids')
    def _compute_recompense_levels(self): 

       for record in self:
            total_amount = sum(voyage.montant for voyage in record.voyage_ids) #Calculer les dépenses totales de voyages du contact (utilisateur) pour définir son niveau de récompense.
            if total_amount < 50000 :
                record.recompense_levels = 'argent'
            elif total_amount  >= 50000 and total_amount  < 100000 :
                record.recompense_levels = 'or'
            elif total_amount >= 100000 :
                record.recompense_levels = 'platine'
