from turtle import width
import cv2 as cv
import numpy as np
import cvzone as cvz

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def getBoard(img, points):
    width, height = int(451 * 1.5), int(451 * 1.5)
    points2 = np.float32([[0, height / 2,], [width, height / 2], [width / 2, 0], [width / 2, height]])
    matrix = cv.getPerspectiveTransform(points, points2)
    imgOutput = cv.warpPerspective(img, matrix, (width, height))

    return imgOutput

def startGame(points):
    cam = cv.VideoCapture(0)

    while True:
        check, board = cam.read()
        #board = rescaleFrame(board, 0.25)
        mask_red = cv.inRange(board, (0,0,50), (150,100,255))

        warpedBoard = getBoard(board, points)

        #cv.line(board, points[0], points[1], [0, 255, 0], 2)
        #cv.line(board, points[2], points[3], [0, 255, 0], 2)

        cv.imshow('Warped', warpedBoard)
    
        cv.imshow('video', board)

        key = cv.waitKey(1)
        if key == 27:
            break

    cam.release()