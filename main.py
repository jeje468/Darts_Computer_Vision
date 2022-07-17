from turtle import left, right
import cv2 as cv
import numpy as np
import cvzone as cvz

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


board = cv.imread('Images/board.jpg')
board = rescaleFrame(board, 0.25)

blur = cv.GaussianBlur(board, (5, 5), 0)


mask_red = cv.inRange(board, (0,0,50), (150,100,255))
mask_post_it = cv.inRange(board, (120,60,50), (200,150,100))
board_contours, contourFound = cvz.findContours(board, mask_post_it, 1000)

left_center = contourFound[0]['center']
right_center = contourFound[3]['center']
top_center = contourFound[1]['center'] if contourFound[1]['center'][1] < contourFound[2]['center'][1] else contourFound[2]['center']
bottom_center = contourFound[1]['center'] if contourFound[1]['center'][1] > contourFound[2]['center'][1] else contourFound[2]['center']
cv.line(board, left_center, right_center, [0, 255, 0], 2)
cv.line(board, top_center, bottom_center, [0, 255, 0], 2)

cv.imshow('Board', board)
cv.moveWindow('Board', 50,50)
cv.imshow('Mask red', mask_red)
cv.imshow('Mask PostIt', mask_post_it)
cv.imshow('Board contours', board_contours)


cv.waitKey(0)