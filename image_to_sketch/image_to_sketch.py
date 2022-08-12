import cv2

image = cv2.imread("image_6.jpeg")
gray_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray_filter)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
inverted_blur = cv2.bitwise_not(blur)
sketch_filter = cv2.divide(gray_filter, inverted_blur, scale=256.0)

cv2.imwrite("sketch_6.jpeg", sketch_filter)

