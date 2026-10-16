# reading image
# import cv2 as cv

# img = cv.imread("Photos/cat.jpg")

# cv.imshow("CAT", img)

# cv.waitKey(0)

# read image bigger than monitor dimension
# import cv2 as cv

# img = cv.imread("Photos/cat_large.jpg")

# cv.imshow("Cat", img)

# cv.waitKey(0)

# reading a video
import cv2 as cv

capture = cv.VideoCapture("Videos/dog.mp4")

while True:

    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
