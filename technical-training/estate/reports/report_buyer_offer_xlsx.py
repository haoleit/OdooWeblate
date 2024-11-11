import io
import xlsxwriter
from odoo import models


class EstatePropertyXlsxReport(models.AbstractModel):
    _name = 'report.estate.buyer_offers_xlsx_report'
    _inherit = 'report.report_xlsx.abstract'

    def create_excel_report(self, start_date, end_date, buyer_id):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Buyer Offers')
        
        # Define formats
        bold = workbook.add_format({'bold': True, 'align': 'center', 'bg_color': '#1F497D', 'font_color': '#FFFFFF'})
        header_format = workbook.add_format({'bold': True, 'bg_color': '#1F497D', 'font_color': '#FFFFFF', 'align': 'center'})
        currency_format = workbook.add_format({'num_format': '#,##0.00', 'align': 'center'})
        date_format = workbook.add_format({'align': 'center'})
        cell_centered = workbook.add_format({'align': 'center'})
        
        # Set column widths
        sheet.set_column('A:A', 20)  # Buyer name
        sheet.set_column('B:B', 25)  # Email
        sheet.set_column('C:H', 15)  # Other columns
        sheet.set_column('I:I', 18)  # Max Price Offer
        sheet.set_column('J:J', 18)  # Min Price Offer
        
        # Header Title
        sheet.merge_range('A5:I5', 'Report Buyer Offers', bold)
        sheet.write('C8', 'Date From', bold)
        sheet.write('D8', start_date.strftime('%d/%m/%Y'), date_format)
        sheet.write('E8', 'Date To', bold)
        sheet.write('F8', end_date.strftime('%d/%m/%Y'), date_format)

        # Column headers
        headers = ['Buyer', 'Email', 'Property Accepted', 'Property Sold', 'Property Cancel', 
                'Offer Accepted', 'Offer Rejected', 'Max Price Offer', 'Min Price Offer']
        for col, header in enumerate(headers):
            sheet.write(11, col, header, header_format)

        # Search for property and report data
        domain = [
        ('date_availability', '>=', start_date),
        ('date_availability', '<=', end_date),
    ]
        if buyer_id:
            domain.append(('buyer_id', '=', buyer_id))

        buyer_ids = self.env['estate.property'].search(domain).mapped('buyer_id').ids
        
        records = self.env['report.buyer.offer'].search([
            ('buyer_id', 'in', buyer_ids)
        ])

        # Write data to Excel
        row = 12  # Starting row for data entries
        for record in records:
            sheet.write(row, 0, record.buyer_id.name or '', cell_centered)
            sheet.write(row, 1, record.buyer_id.email or '', cell_centered)
            sheet.write(row, 2, record.property_accepted or 0, cell_centered)
            sheet.write(row, 3, record.property_sold or 0, cell_centered)
            sheet.write(row, 4, record.property_cancel or 0, cell_centered)
            sheet.write(row, 5, record.offer_accepted or 0, cell_centered)
            sheet.write(row, 6, record.offer_rejected or 0, cell_centered)
            sheet.write(row, 7, record.max_price_offer or 0, currency_format)
            sheet.write(row, 8, record.min_price_offer or 0, currency_format)
            row += 1

        # Close workbook and prepare output
        workbook.close()
        output.seek(0)
        
        return output.getvalue()