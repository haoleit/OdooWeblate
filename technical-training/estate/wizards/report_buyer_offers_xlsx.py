from odoo import api, models, fields
from odoo.exceptions import ValidationError

class BuyerOfferExportXlsxWizard(models.TransientModel):
    _name = 'buyer.offer.export.xlsx.wizard'
    _description = 'Buyer Offer XLSX Wizard'

    start_date = fields.Date(string="Date From", required=True)
    end_date = fields.Date(string="Date To", required=True)
    buyer_ids = fields.Many2many('res.partner', string="Buyers")

    @api.constrains('start_date', 'end_date')
    def _check_date_range(self):
        for record in self:
            if record.end_date and record.start_date and record.end_date < record.start_date:
                raise ValidationError("The end date must be greater than the start date.")

    def action_export_excel(self):
        # Gọi controller để xuất báo cáo
        buyer_ids = ','.join(map(str, self.buyer_ids.ids)) if self.buyer_ids else ''
        return {
            'type': 'ir.actions.act_url',
            'url': f'/estate/buyer_offer_report_xlsx?start_date={self.start_date}&end_date={self.end_date}&buyer_ids={buyer_ids}',
            'target': 'self',
        }
