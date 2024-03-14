from PyPDF2 import PdfWriter, PdfReader
# page numbering starts from 0
start=51  #start
end=71 #end SHOULD BE ACTUAL PAGE NUMBER
infile = PdfReader('SEM 4 ANSWERS.pdf', 'rb')
output = PdfWriter()

for i in range(start, end):
    p = infile.pages[i] 
    output.add_page(p)

with open('Android_Dev_22-23_answer.pdf', 'wb') as f:
    output.write(f)