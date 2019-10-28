# -*- coding: utf-8 -*-

from openerp import netsvc, tools, pooler
from openerp.tools.translate import _
from openerp import models, fields, api
import time

class pos_cashier(models.Model):
    _name = 'pos_cashier.pos_cashier'
    _order = 'cashier_name asc'

    pos_config_id = fields.Many2one('pos.config', 'Point De Vente', required=True)
    cashier_name = fields.Char('Caissier', size=128, required=True)
    active = fields.Boolean('Active', help="Si le caissier n'est pas active il ne sera pas en fonction dans le POS")

    _defaults = {
        'cashier_name': '',
        'active': True,
        'pos_config_id': lambda self, cr, uid, c: self.pool.get('res.users').browse(cr, uid, uid, c).pos_config.id,
    }

    _sql_constraints = [
        ('uniq_name', 'unique(cashier_name, pos_config_id)', "Un caissier existe deja avec ce nom dans ce point de vente"),
    ]

class inherit_pos_order_for_cashiers(models.Model):
    _name='pos.order'
    _inherit='pos.order'

    cashier_name = fields.Char('Caissier', size=128)

    def create_from_ui(self, cr, uid, orders, context=None):
        # _logger.info("orders: %r", orders)
        order_ids = []

        for tmp_order in orders:
            order = tmp_order['data']
            order_id = self.create(cr, uid, {
            'name': order['name'],
            'user_id': order['user_id'] or False,
            'session_id': order['pos_session_id'],
            'lines': order['lines'],
            'pos_reference': order['name'],
            'cashier_name': order['cashier_name']
        }, context)
            

            for payments in order['statement_ids']:
                payment = payments[2]
                self.add_payment(cr, uid, order_id, {
                    'amount': payment['amount'] or 0.0,
                    'payment_date': payment['name'],
                    'statement_id': payment['statement_id'],
                    'payment_name': payment.get('note', False),
                    'journal': payment['journal_id']
                }, context=context)
            if order['amount_return']:
                session = self.pool.get('pos.session').browse(cr, uid, order['pos_session_id'],context=context)
                cash_journal = session.cash_journal_id
                cash_statement = False
                if not cash_journal:
                    cash_journal_ids = filter(lambda st: st.journal_id.type == 'cash', session.statement_ids)
                    if not len(cash_journal_ids):
                        raise models.except_models(_('error!'),

    _("No cash statement found for this session. Unable to record returned cash."))
                    cash_journal = cash_journal_ids[0].journal_id
                self.add_payment(cr, uid, order_id, {
                    'amount': -order['amount_return'],
                    'payment_date': time.strftime('%Y-%m-%d %H:%M:%S'),
                    'payment_name': _('return'),
                    'journal': cash_journal.id,}, context=context)
            order_ids.append(order_id)
            wf_service = netsvc.LocalService("workflow")
            wf_service.trg_validate(uid, 'pos.order', order_id, 'paid', cr)
        return order_ids