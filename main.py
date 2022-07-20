from tkinter import *
import cv2 as cv
import numpy as np
import cvzone as cvz
from PIL import ImageTk, Image
from pip import main
from gameplay import *

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def setValues():
    board = cv.imread('Images/calibration.jpg')
    #board = rescaleFrame(board, 0.25)
    B = dark_B.get()
    mask_post_it = cv.inRange(board, (dark_B.get(),dark_G.get(),dark_R.get()), (light_B.get(),light_G.get(),light_R.get()))

    cv.imshow('Mask', mask_post_it)

    return mask_post_it

def findCenterPointsOfPostIt(mask):
    board_contours, contourFound = cvz.findContours(image, mask, 100)

    cv.imshow('Contour', board_contours)

    if len(contourFound) >= 4:
        left_center = contourFound[0]['center']
        right_center = contourFound[3]['center']
        top_center = contourFound[1]['center'] if contourFound[1]['center'][1] < contourFound[2]['center'][1] else contourFound[2]['center'] 
        bottom_center = contourFound[1]['center'] if contourFound[1]['center'][1] > contourFound[2]['center'][1] else contourFound[2]['center']
            
        points = np.float32([[left_center[0], left_center[1]], [right_center[0], right_center[1]], [top_center[0], top_center[1]], [bottom_center[0], bottom_center[1]]])
        
        return points


def start():
    mask = setValues()
    points = findCenterPointsOfPostIt(mask)
    startGame(points)


camera = cv.VideoCapture(0)
result, image = camera.read()
if result:
    cv.imwrite('Images/calibration.jpg', image)

master = Tk()
dark_B = Scale(master, from_=0, to=255, length=400, orient=HORIZONTAL)
dark_B.set(120)
dark_B.pack()
dark_G = Scale(master, from_=0, to=255, length=400, orient=HORIZONTAL)
dark_G.set(60)
dark_G.pack()
dark_R = Scale(master, from_=0, to=255, length=400, orient=HORIZONTAL)
dark_R.set(50)
dark_R.pack()

light_B = Scale(master, from_=0, to=255, length=400, orient=HORIZONTAL)
light_B.set(200)
light_B.pack()
light_G = Scale(master, from_=0, to=255, length=400, orient=HORIZONTAL)
light_G.set(150)
light_G.pack()
light_R = Scale(master, from_=0, to=255, length=400, orient=HORIZONTAL)
light_R.set(100)
light_R.pack()

Button(master, text='Show', command=setValues).pack()
Button(master, text='Start game', command=start).pack()


mainloop()

