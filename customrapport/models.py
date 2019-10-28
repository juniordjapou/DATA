# -*- coding: utf-8 -*-

from openerp import models, fields, api

class customrapport(models.Model):
    _name = 'customrapport.customrapport'

    name = fields.Char('Name', required=True)
    surname = fields.Char('surname', required=True)