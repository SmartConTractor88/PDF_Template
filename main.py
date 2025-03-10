import pandas as pd
# import fpdf
from fpdf import FPDF # a class that creates PDF instances

# define the PDF

df = pd.read_csv("topics.csv")


pdf = FPDF(orientation="P", unit="mm", format="A4") # P for portrait, L for landscape

pdf.add_page() # add a page

pdf.set_font(family="Times", style="B", size=24)

pdf.cell(w=0, h=24, txt="PDF Template", align="C", ln=1, border=1)
pdf.cell(w=0, h=24, txt="", align="C", ln=1, border=0) # empty cell

pdf.set_font(family="Times", size=18)

pdf.cell(w=0, h=24, txt="PDF Template", align="C", ln=1, border=1)

for index, row in df.iterrows():
    pdf.add_page() # add a page
    print(row["Topic"])
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=24, txt=row["Topic"], align="C", ln=1, border=1)
    pdf.line(20, 27, 190, 27)
    
pdf.output("first_pdf.pdf")