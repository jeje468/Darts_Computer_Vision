import cv2 as cv
import cv2 as cv
import numpy as np
import cvzone as cvz

original = cv.imread('Images/board_regular.JPG')
new = cv.imread('Images/board_with_dart.JPG')

diff = original.copy()
cv.absdiff(original, new, diff)
gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)

#cv.imshow('Difference', gray)



(thresh, mask) = cv.threshold(gray, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow('Original ask', mask)

kernel = np.ones((7,7), np.uint8)
mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
mask = cv.medianBlur(mask, 9)
mask = cv.dilate(mask, kernel, iterations=4)
kernel = np.ones((9,9), np.uint8)
mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
cv.imshow('Mask', mask)


board_contours, contourFound = cvz.findContours(new, mask, 1000)
cv.imshow('Contours', board_contours)


cv.waitKey(0)

