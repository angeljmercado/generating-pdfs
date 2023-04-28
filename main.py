from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

csv = pd.read_csv("topics.csv")

for index, row in csv.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 255)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)
    for i in range(int(row["Pages"] - 1)):
        pdf.add_page()

# pdf.set_font(family="Times", size=10)
# pdf.cell(w=10, h=12, txt="Hello There!2", align="L", ln=1)
pdf.output("output.pdf")

