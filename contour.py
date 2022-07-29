import cv2 as cv
import cv2 as cv
import numpy as np
import cvzone as cvz

def retrieveDartContour(board, dart):
    #board = cv.imread('Images/board_regular.JPG')
    #dart = cv.imread('Images/board_with_dart.JPG')

    diff = board.copy()
    cv.absdiff(board, dart, diff)
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


    board_contours, contourFound = cvz.findContours(dart, mask, 1000)
    cv.imshow('Contours', board_contours)

    return mask, contourFound

