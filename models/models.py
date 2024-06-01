# -*- coding: utf-8 -*-

from odoo import models, fields, api

class fct_alumno(models.Model):
    _name = 'fct.alumno'

    name = fields.Char(string="Código", required=True, help="Introduzca el código")
    nombre = fields.Char(string="Nombre", required=True, help="Introduzca el nombre")
    apellidos = fields.Char(string="Apellidos", required=True, help="Introduzca los apellidos")
    fechanacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    cicloformativo = fields.Selection([('0', 'SMR'), ('1', 'DAM'), ('2', 'DAW'), ('3', 'ASIR')], string="Ciclo formativo")
    notamedia = fields.Float(string="Nota media", help="Introduzca la nota media")
    notmed = fields.Char(string="Nota media", compute="_notmed", store=True)
    empresa = fields.Many2one("fct.empresa", string="Empresa", ondelete="no action")

    @api.depends('notamedia') 
    def _notmed(self): 
        for record in self: 
            if record.notamedia < 5:
                record.notmed = "Suspenso"
            elif  5 <= record.notamedia <= 6.9:
                record.notmed = "Aprobado"
            elif  7 <= record.notamedia <= 8.9:
                record.notmed = "Notable"
            else:
                record.notmed = "Sobresaliente"

class fct_empresa(models.Model):
    _name = 'fct.empresa'

    name = fields.Char(string="Nombre", required=True, help="Introduzca el nombre")
    direccion = fields.Char(string="Dirección", required=True, help="Introduzca la dirección")
    listadealumnos = fields.One2many("fct.alumno", "empresa", string="Listado de alumnos que han hecho prácticas en esta empresa")
