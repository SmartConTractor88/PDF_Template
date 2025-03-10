import pandas as pd
# import fpdf
from fpdf import FPDF # a class that creates PDF instances

# define the PDF

df = pd.read_csv("topics.csv")


pdf = FPDF(orientation="P", unit="mm", format="A4") # P for portrait, L for landscape



for index, row in df.iterrows():
    
    pdf.add_page() # add a page

    print(row["Topic"])
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=0, h=24, txt=row["Topic"], align="C", ln=1, border=0)
    pdf.line(30, 28, 180, 28)
    
    for page in range(row["Pages"] - 1):
        pdf.add_page() # add a page
    
pdf.output("first_pdf.pdf")