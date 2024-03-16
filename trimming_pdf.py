from PyPDF2 import PdfWriter, PdfReader
# page numbering starts from 0
start = 2  #start
end = 3 #end SHOULD BE ACTUAL PAGE NUMBER
infile = PdfReader('fff.pdf', strict=False)
output = PdfWriter()

for i in range(start, end):
    p = infile.pages[i] 
    output.add_page(p)

with open('Theory_Time_Table.pdf', 'wb') as f:
    output.write(f)