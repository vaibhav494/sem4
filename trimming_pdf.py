from PyPDF2 import PdfWriter, PdfReader
# page numbering starts from 0
start = 35  #start
end = 38 #end SHOULD BE ACTUAL PAGE NUMBER
infile = PdfReader('portion.pdf', 'rb')
output = PdfWriter()

for i in range(start, end):
    p = infile.pages[i] 
    output.add_page(p)

with open('Android_portion.pdf', 'wb') as f:
    output.write(f)