from PyPDF2 import PdfFileReader, PdfFileWriter

reader = PdfFileReader('doc.pdf', 'r')
reader2 = PdfFileReader('doc.pdf', 'r')
writer = PdfFileWriter()
for i in range(reader.getNumPages()):
    page1 = reader.getPage(i)
    page2 = reader2.getPage(i)
    page1.cropBox.setLowerLeft((0,0))
    page1.cropBox.setUpperRight((515.88,728.4))
    page2.cropBox.setLowerLeft((515.88,0))
    page2.cropBox.setUpperRight((1031.76,728.4))
    writer.addPage(page1)
    writer.addPage(page2)

output = open('doc_cropped.pdf', 'wb')
writer.write(output)
output.close()
print("Document has been cropped successfully")
