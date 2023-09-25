from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

for pdf in os.listdir(os.curdir):
    if pdf.endswith(".pdf"):
        print(pdf)
        merger.append(pdf)
    
merger.write("output.pdf")