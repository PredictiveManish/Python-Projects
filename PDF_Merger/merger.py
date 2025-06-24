import PyPDF2

files_count = int(input("Enter the number of PDF to merge: "))

files = []

for i in range(files_count):
    file = input("Enter the file address: ")
    files.append(file)

merger = PyPDF2.PdfMerger()

for file in files:
    merger.append(file)
output_folder = "C://Users/manis/Downloads/"

filename = input("Enter output file name: ")
output_path = f"{output_folder}{filename}.pdf"
merger.write(output_path)
merger.close()

print("PDF files merged successfully!")