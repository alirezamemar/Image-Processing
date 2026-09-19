import cv2 as cv
import numpy as np

blank_image = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("blank", blank_image)

# blank_image[:] = 0, 255, 0
# cv.imshow("Green", blank_image)

# create a square with cv:
# blank_image[200:300, 300:400] = 0, 0, 255
# cv.imshow("Red", blank_image)

# cv.rectangle(blank_image, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
# cv.rectangle(blank_image, (0, 0),
#              (blank_image.shape[1]//2, blank_image.shape[0]//2), (0, 255, 0))


# create circle
# cv.circle(blank_image, (250, 250), 40, (0, 255, 0), thickness=2)
# cv.imshow("Circle", blank_image)

# create a line
# cv.line(blank_image, (0, 0), (250, 250), (255, 0, 0), thickness=2)
# cv.imshow("Line", blank_image)
cv.putText(blank_image, 'Hello', (225, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank_image)


cv.waitKey(0)
