
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class informacion(models.Model):
     _name = 'odoo_basico.informacion'
     _description = 'Exemplo de odoo basico'
     _sql_constraints = [('nomeUnico', 'unique(name)', 'Non se pode repetir o Título')]
     _order = "descripcion desc"

     name = fields.Char(string="Título:")
     descripcion = fields.Text(string="A descripción:")
     alto_en_cms = fields.Integer(string="Alto en Centímetros")
     longo_en_cms = fields.Integer(string="Longo en Centímetros")
     ancho_en_cms = fields.Integer(string="Ancho en Centímetros")
     volume = fields.Float(compute="_volume", store=True)
     peso = fields.Float(string="Peso en Kgs.",default=2.7,digits=(6,2))
     densidade = fields.Float(compute="_densidade", store=True)
     literal = fields.Char(store=False)
     autorizado = fields.Boolean(string="¿Autorizado?", default=True)
     sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')],string="Sexo")
     foto = fields.Binary(string='Foto')
     adxunto_nome = fields.Char(string="Nome Adxunto")
     adxunto = fields.Binary(string="Arquivo adxunto")

     @api.depends('alto_en_cms', 'longo_en_cms', 'ancho_en_cms')
     def _volume(self):
          for rexistro in self:
               rexistro.volume = float(rexistro.alto_en_cms) * float(rexistro.longo_en_cms) * float(
                    rexistro.ancho_en_cms)

     @api.depends('volume', 'peso')
     def _densidade(self):
          for rexistro in self:
               if rexistro.volume !=0:
                    rexistro.densidade = 100 * (float(rexistro.peso) / float(rexistro.volume))
               else:
                    rexistro.densidade = 0

     @api.onchange('alto_en_cms')
     def _avisoAlto(self):
          for rexistro in self:
               if rexistro.alto_en_cms > 7:
                    rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cms
               else:
                    rexistro.literal = ""

     @api.constrains('peso')  # Ao usar ValidationError temos que importar a libreria ValidationError
     def _constrain_peso(self):  # from odoo.exceptions import ValidationError
          for rexistro in self:
               if rexistro.peso < 1 or rexistro.peso > 4:
                    raise ValidationError('Os peso de %s ten que ser entre 1 e 4 ' % rexistro.name)