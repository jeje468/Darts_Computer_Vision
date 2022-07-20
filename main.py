from tkinter import *
import cv2 as cv
from PIL import ImageTk, Image
from pip import main

from gameplay import start_game

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def set_values():
    board = cv.imread('Images/calibration.jpg')
    board = rescaleFrame(board, 0.25)
    B = dark_B.get()
    mask_post_it = cv.inRange(board, (dark_B.get(),dark_G.get(),dark_R.get()), (light_B.get(),light_G.get(),light_R.get()))

    cv.imshow('Mask', mask_post_it)

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

Button(master, text='Show', command=set_values).pack()
Button(master, text='Start game', command=start_game()).pack()


#mainloop()

