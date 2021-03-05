# -*- coding: utf-8 -*-

from odoo import models,fields,api

class ventana(models.Model):
    _name = "ventanas.ventana"
    _descripcion = "modelo de ventana"

    name = fields.Char("Nombre")
    ubicacion = fields.Char("ubicacion")
    precio = fields.Float("Precio")
    medida = fields.Selection([("pulg","Pulgadas"),("mm", "Milimetros")])
    ancho = fields.Integer("Ancho")
    alto = fields.Integer("Alto")
    area = fields.Float("Area", compute="_area_pc", store=True)
    sistema = fields.Many2one("ventanas.sistema", "Sistema", required=False)

    @api.depends('ancho','alto')
    def _area_pc(self):
        self.area = self.ancho * self.alto / 1000000


class Sistema(models.Model):
    _name ="ventanas.sistema"
    _description = "Sistemas"

    name= fields.Char("Codigo")
    description = fields.Char("Descripcion")
