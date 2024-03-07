from PyPDF2 import PdfWriter, PdfReader
pages_to_keep = [5, 6] # page numbering starts from 0
infile = PdfReader('SYBSC Sem IV Regular Mar 2023.pdf', 'rb')
output = PdfWriter()

for i in pages_to_keep:
    p = infile.pages[i] 
    output.add_page(p)

with open('Adv_Java_22-23.pdf', 'wb') as f:
    output.write(f)