import cv2
import pytesseract

#define exe file path for connection
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

#read our image
img = cv2.imread('out.png')

#pytesseract accepts only rgb values
#we should convert it
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#image to string
print(pytesseract.image_to_string(img))
#show
cv2.imshow('image_name', img)
cv2.waitKey(0)


