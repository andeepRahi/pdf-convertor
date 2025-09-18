from fpdf import FPDF
import pandas as pd

pdf= FPDF(orientation='P', unit='mm', format='A4')
df = pd.read_csv('topics.csv')
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Arial', style="B",size=24)
    pdf.set_text_color(0,0,0)
    pdf.cell(w=0, h=12, txt=row['Topic'],align="L", ln=1)
    for y in range(20,298,10):
        pdf.line(10,y,200,y)

   #set footer
    pdf.ln(265)
    pdf.set_font('Arial', style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(0,10,txt=row['Topic'],align="R", ln=1)

    for i in range(row['Pages']-1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font('Arial', style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, txt=row['Topic'], align="R", ln=1)
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output('output.pdf')