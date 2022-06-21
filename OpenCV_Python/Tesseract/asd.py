import cv2
import pytesseract

img = cv2.imread('out.png')

# Adding custom options
# custom_config = r'--oem 3 --psm 6'
custom_config = r'--oem 3 '
custom_config = r'--psm 7 -l fin'
text = pytesseract.image_to_string(img, config=custom_config)

print("Tulos: %s" % text.split('\n')[0])