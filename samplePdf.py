from fpdf import FPDF
import sqlite3
con=sqlite3.connect("college.db")
cur=con.cursor()
sql="select *from course_info"
cur.execute(sql)
pdf=FPDF()
for row in cur.fetchall():
    #print(row[1],row[2],row[3])       
    pdf.add_page("a4")
    pdf.image('certificate.jpg', 10, 8, 250)
    pdf.set_font('Arial', 'B', 16)

    pdf.ln(70)
    pdf.cell(90, 10, '',0,0,"C")
    pdf.cell(100, 10, row[1],0,0,"C")

    pdf.ln(40)
    pdf.cell(90, 10, '',0,0,"C")
    pdf.cell(100, 10, row[2],0,0,"C")

    pdf.ln(20)
    pdf.cell(60, 10, '',0,0,"C")
    pdf.cell(40, 10, row[3],0,0,"C")
    pdf.image('mysign.png', 193, 135, 40)
    
pdf.output("a.pdf","F")

