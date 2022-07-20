import cv2 as cv
import numpy as np

def get_board(img, points):
    width, height = int(451 * 1.5), int(451 * 1.5)
    points1 = np.float32(points)
    points2 = np.float32([[0, height / 2,], [width, height / 2], [width / 2, 0], [width / 2, height]])
    matrix = cv.getPerspectiveTransform(points1, points2)
    imgOutput = cv.warpPerspective(img, matrix, (width, height))

    return imgOutput

img = cv.imread('Images/board.jpg')
points = np.float32([[517, 2209],[2481, 2121],[1669, 1037],[1773, 3341]])
warpedImage = get_board(img, points)
cv.imshow('Warped', warpedImage)

cv.waitKey(0)