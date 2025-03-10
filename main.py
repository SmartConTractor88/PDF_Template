# import pandas
# import fpdf
from fpdf import FPDF # a class that creates PDF instances

# define the PDF
pdf = FPDF(orientation="P", unit="mm", format="A4") # P for portrait, L for landscape

pdf.add_page() # add a page

pdf.set_font(family="Times", style="B", size=24)

pdf.cell(w=0, h=24, txt="PDF Template", align="C", ln=1, border=1)
pdf.cell(w=0, h=24, txt="", align="C", ln=1, border=0) # empty cell

pdf.set_font(family="Times", size=18)

pdf.cell(w=0, h=24, txt="PDF Template", align="C", ln=1, border=1)

pdf.add_page() # add a page

pdf.set_font(family="Times", style="B", size=24)

pdf.cell(w=0, h=24, txt="PDF Template", align="C", ln=1, border=1)

pdf.output("first_pdf.pdf")

