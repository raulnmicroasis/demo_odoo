
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class lineapedido(models.Model):
     _name = 'odoo_basico.lineapedido'
     _description = 'Exemplo de linea de pedido'

     name = fields.Char(string="Nome da Linea pedido:",required=True,size=20)
     descripcion_da_lineapedido = fields.Text(string="A descripción")
     # Os campos Many2one crean un campo na BD
     pedido_id = fields.Many2one('odoo_basico.pedido',ondelete="cascade", required=True)
     # Os campos Many2many crean unha táboa na BD
     informacion_ids = fields.Many2many("odoo_basico.informacion",
                                        string="Rexistro de Información",
                                        relation="odoo_basico_lineapedido_informacion",
                                        column1="lineapedido_id", column2="informacion_id")