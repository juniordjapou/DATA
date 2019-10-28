# -*- coding: utf-8 -*-

from openerp import models, fields, api

class module(models.Model):
    _name = 'module.module'
    # _rec_name = 'Auteur'

    first_name = fields.Char(string='FirstName', required=True)
    last_name = fields.Char(string='LastName', required=True)
    book_ids = fields.One2many('book.book', 'author_id', 'Books')

    @api.model
    def create(self, values):
        # Add code here
        return super(module, self).create(values)

class book(models.Model):
    _name = 'book.book'
    # _rec_name = 'Book'

    title = fields.Char('Title', required=True)
    genre = fields.Char('Genre', required=True)
    author_id = fields.Many2one('module.module', 'Module', ondelete='cascade')



