import cv2 as cv
import numpy as np
import cvzone as cvz
from cvzone.ColorModule import ColorFinder

def start_game(Dark_B, Dark_G, Dark_R, Light_B, Light_G, Light_R):
    cam = cv.VideoCapture(0)
    colorfinder = ColorFinder(True)

    while True:
        check, board = cam.read()

        mask_red = cv.inRange(board, (0,0,50), (150,100,255))
        mask_post_it = cv.inRange(board, (Dark_B,Dark_G,Dark_R), (Light_B,Light_G,Light_R))
        board_contours, contourFound = cvz.findContours(board, mask_post_it, 1000)

        cv.imshow('video', board)
        cv.imshow('mask', mask_post_it)


        if len(contourFound) >= 4:
            left_center = contourFound[0]['center']
            right_center = contourFound[3]['center']
            top_center = contourFound[1]['center'] if contourFound[1]['center'][1] < contourFound[2]['center'][1] else contourFound[2]['center']
            bottom_center = contourFound[1]['center'] if contourFound[1]['center'][1] > contourFound[2]['center'][1] else contourFound[2]['center']
            cv.line(board, left_center, right_center, [0, 255, 0], 2)
            cv.line(board, top_center, bottom_center, [0, 255, 0], 2)
    
        cv.imshow('video', board)

        key = cv.waitKey(1)
        if key == 27:
            break

    cam.release()