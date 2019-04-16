import cv2

x1 = 650
x2 = 1279
y1 = 0
y2 = 718
img = cv2.imread('crop_pic.jpg', 0)
crop_img = img[y1:y2, x1:x2]
cv2.imshow('image', img)
cv2.imshow('cropped', crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
