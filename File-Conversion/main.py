from tkinter import Tk, Button, filedialog, messagebox
from docx2pdf import convert as docx2pdf_convert
from pdf2image import convert_from_path
from pdf2docx import Converter
from PIL import Image
import os
# file dialog
# downloads = os.path.join(os.path.expanduser("~"),"Downloads")
downloads = os.path.join(os.path.expanduser("~"), "Downloads")

def word_to_pdf():
    file = filedialog.askopenfilename(filetypes=[("Word files","*.docx")])
    if file:
        docx2pdf_convert(file, downloads)
        messagebox.showinfo("Successful", f"Saved in {downloads}")

def pdf_to_word():
    file = filedialog.askopenfilename(filetypes=[("PDF files","*.pdf")])
    if file:
        cv = Converter(file)
        output = os.path.join(downloads, os.path.basename(file).replace(".pdf",".docx"))
        cv.convert(output)
        cv.close()
        messagebox.showinfo("Successful", f"Saved in {downloads}")
def jpg_to_pdf():
    file = filedialog.askopenfilename(filetypes=[("Image files","*.jpg;*.jpeg;*.png")])
    if file:
        img = Image.open(file).convert("RGB")
        output = os.path.join(downloads, os.path.basename(file).split(".")[0] + ".pdf" )
        img.save(output)
        messagebox.showinfo("Successful", f"Saved in {downloads}")

def pdf_to_jpg():
    file = filedialog.askopenfilename(filetypes=[("PDF files","*.pdf")])
    if file:
        images = convert_from_path(file)
        for i, img in enumerate(images):
            output = os.path.join(downloads, f"{os.path.basename(file)}_page{i+1}.jpg")
            img.save(output,"JPEG")
        messagebox.showinfo("Successful",f"Saved in {downloads}")

root = Tk()
root.title("Mini File Converter")

Button(root, text="Word -> PDF", command=word_to_pdf).pack(pady=5)
Button(root, text="PDF -> Word", command=pdf_to_word).pack(pady=5)
Button(root, text="JPG → PDF", command=jpg_to_pdf).pack(pady=5)
Button(root, text="PDF → JPG", command=pdf_to_jpg).pack(pady=5)

root.mainloop()