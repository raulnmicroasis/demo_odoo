from odoo import models, fields, api


class inventario(models.Model):
    _name = 'odoo_basico.inventario'
    _description = 'Listado actual del inventario'

    nombre = fields.Char(string="Nombre:")
    nombre_comercial = fields.Char(string="Nombre comercial:")
    stock_actual= fields.Float(string="Stock actual", default=0.0, digits=(6, 2))
