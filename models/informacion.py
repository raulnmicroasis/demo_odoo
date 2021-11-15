
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
     _name = 'odoo_basico.informacion'
     _description = 'Exemplo de odoo basico'

     name = fields.Char(string="Título:")
     descripcion = fields.Text(string="A descripción:")
     alto_en_cms = fields.Integer(string="Alto en Centímetros")
     longo_en_cms = fields.Integer(string="Longo en Centímetros")
     ancho_en_cms = fields.Integer(string="Ancho en Centímetros")
     peso = fields.Float(string="Peso en Kgs.",default=2.7,digits=(6,2))
     autorizado = fields.Boolean(string="¿Autorizado?", default=True)
     sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')],string="Sexo")