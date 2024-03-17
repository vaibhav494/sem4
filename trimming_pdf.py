from PyPDF2 import PdfWriter, PdfReader
# page numbering starts from 0
start = 576  #start
end = 609 #end SHOULD BE ACTUAL PAGE NUMBER
infile = PdfReader('Textbook.pdf', strict=False)
output = PdfWriter()

for i in range(start, end):
    p = infile.pages[i] 
    output.add_page(p)

with open('chapter 18.pdf', 'wb') as f:
    output.write(f)