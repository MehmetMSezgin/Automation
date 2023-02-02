import cv2

img = cv2.imread('lena.jpg', -1)
print(img)
cv2.imshow('image', img)
k = cv2.waitKey(0)   #how many second it will wait

if k == 27:     #it means esc button
    cv2.destroyAllWindows()
elif k == ord('s'):  #if you push save button it will save
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()

