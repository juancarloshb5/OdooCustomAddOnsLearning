# -*- coding: utf-8 -*-

from odoo import models,fields

class ventana(models.Model):
    _name = "ventanas.ventana"
    _descripcion = "modelo de ventana"

    name = fields.Char("Id")
    ubicacion = fields.Char("ubicacion")
    precio = fields.Float("Precio")


# class ventanas(models.Model):
#     _name = 'ventanas.ventanas'
#     _description = 'ventanas.ventanas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
