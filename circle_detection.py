import cv2 as cv
import numpy as np

image = cv.imread('Images/board.jpg')
output = image.copy()
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imshow('Board', image)

# detect circles in the image
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1.2, 100)
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv.circle(output, (x, y), r, (0, 255, 0), 4)
		cv.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# show the output image
	cv.imshow("output", np.hstack([image, output]))
	cv.waitKey(0)