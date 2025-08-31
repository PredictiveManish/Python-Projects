import pymupdf

doc = pymupdf.open("syllabus.pdf")

output = open("output.txt","wb")
for page in doc:
    text = page.get_text().encode("utf8")
    output.write(text)
    output.write(bytes((12,)))
output.close()