import pandas as pd
# import fpdf
from fpdf import FPDF # a class that creates PDF instances

# define the PDF

df = pd.read_csv("topics.csv")


pdf = FPDF(orientation="P", unit="mm", format="A4") # P for portrait, L for landscape
pdf.set_auto_page_break(auto=False, margin=0) # pages should not be broken automatically

for index, row in df.iterrows():
    
    pdf.add_page() # add a page

    print(row["Topic"])
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=24, txt=row["Topic"], align="C", ln=1, border=0)
    pdf.line(30, 28, 180, 28)

    pdf.ln(250) # 250 mm of break lines

    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="C", ln=1, border=0)

    for y in range(50, 288, 10):
        pdf.line(20, y, 200, y)  # create lines for handwriting
    
    for page in range(row["Pages"] - 1):
        pdf.add_page() # add a page

        

        pdf.ln(274) # 250 mm of break lines

        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="C", ln=1, border=0)
    
pdf.output("first_pdf.pdf")