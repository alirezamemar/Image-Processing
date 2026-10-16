import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")

# translation


def translation(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x ---> left
# -y ---> up
# x ---> right
# y ---->down
translated = translation(img, 100, 200)
cv.imshow("translation", translated)
cv.imshow("Park", img)

cv.waitKey(0)
