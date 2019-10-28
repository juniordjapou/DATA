# -*- coding: utf-8 -*-
from openerp import models, fields, api

class moduletest(models.Model):
    _name = 'moduletest.moduletest'

    firstname = fields.Char('FirstName', required=True)
    lastname = fields.Char('LastName', required=True)
    book_ids = fields.One2many(comodel_name='moduletest.book', inverse_name='author_id')

class book(models.Model):
    _name = 'moduletest.book'

    title = fields.Char('Title', required=True)
    genre = fields.Char('Genre', required=True)
    author_id = fields.Many2one(comodel_name='moduletest.moduletest', ondelete='cascade')







