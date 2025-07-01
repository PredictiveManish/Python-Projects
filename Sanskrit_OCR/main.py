import cv2
from PIL import Image
import pytesseract

im_file = "D:\Projects\Python-Projects\Sanskrit_OCR\page.png"
im = Image.open(im_file)
im.show()
im.save("temp/page01.jpg")