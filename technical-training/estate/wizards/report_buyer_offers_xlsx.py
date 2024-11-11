from odoo import models, fields

class BuyerOfferExportXlsxWizard(models.TransientModel):
    _name = 'buyer.offer.export.xlsx.wizard'
    _description = 'Buyer Offer XLSX Wizard'

    start_date = fields.Date(string="Date From", required=True)
    end_date = fields.Date(string="Date To", required=True)

    def action_export_excel(self):
        # Gọi controller để xuất báo cáo
        return {
            'type': 'ir.actions.act_url',
            'url': f'/estate/buyer_offer_report_xlsx?start_date={self.start_date}&end_date={self.end_date}',
            'target': 'self',
        }
