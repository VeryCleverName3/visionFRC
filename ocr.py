import pytesseract
import cv2
from PIL import Image

cap = cv2.VideoCapture(0)

while 1:
    _, frame = cap.read()

    cv2.imshow("frame", frame)

    # If you don't have tesseract executable in your PATH, include the following:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    print(pytesseract.image_to_string(Image.open('C:/Users/hayde/Pictures/nerd.png')))
