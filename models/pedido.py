
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class pedido(models.Model):
     _name = 'odoo_basico.pedido'
     _description = 'Exemplo de pedido'

     name = fields.Char(string="Identificador",required=True,size=20)
     # Os campos One2many Non se almacenan na BD
     lineapedido_ids = fields.One2many("odoo_basico.lineapedido", 'pedido_id')