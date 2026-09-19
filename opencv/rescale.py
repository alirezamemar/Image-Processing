import cv2 as cv


# define a rescale function
def rescaleFrame(frame, scale=0.7):
    # this method can use for images videos and live videos.
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


# resize image
img = cv.imread("Photos/cat_large.jpg")
resized_image = rescaleFrame(img)
cv.imshow("Cat", resized_image)

cv.waitKey(0)

# resize video
# capture = cv.VideoCapture("Videos/dog.mp4")


def changeRes(width, height):
    # This function only can use for live videos
    capture.set(3, width)
    capture.set(4, width)

# while True:

#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)

#     cv.imshow("Video Resized", frame_resized)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
