from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
csv = pd.read_csv("topics.csv")

for index, row in csv.iterrows():
    pdf.add_page()
    # Set the headers
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 255)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    # Set the footers
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    for i in range(int(row["Pages"] - 1)):
        pdf.add_page()
pdf.output("output.pdf")
