import cv2 as cv

img = cv.imread("Photos/cat.jpg")

cv.imshow("Cat", img)
# converting and image to gray-scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("GRAY", gray)

# Blur
blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Edge", canny)

# dilated
dilated = cv.dilate(canny, (7, 7), iterations=7)
cv.imshow("Dilated", dilated)

# Eroded
eroded = cv.erode(dilated, (3, 3), iterations=2)
cv.imshow("Eroded", eroded)

# resize
resize = cv.resize(img, (500, 500))
cv.imshow("Resize", resize)

# crop
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
