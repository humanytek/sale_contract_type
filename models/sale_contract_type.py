from openerp import api, fields, models


class SaleContractType(models.Model):
    _inherit = 'sale.order'

    contract_type = fields.Selection([
        ('axc', 'AxC'),
        ('pf', 'Precio Fijo'),
        ('pm', 'Precio Maximo'),
        ('pd', 'Precio Despues'),
        ('na', 'No aplica'),
    ], default='na', required=True)
