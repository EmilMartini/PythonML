from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np

#Import classes
from perceptron import Perceptron
from point import Point
import random as rnd

#Create visual window
w = 600
h = 600
pointsize = 2
root = Tk()
canvas = Canvas(root, width = w, height = h)
canvas.pack()

#Create ML Stuff
trainingData = []
perceptron = Perceptron(0.1)
canvas.create_line(0,0,w,h)

for i in range(250):
    trainingData.append(Point(rnd.random(), rnd.random()))
    pixelX = trainingData[i].x * w
    pixelY = trainingData[i].y * h
    color = 'black' if trainingData[i].label == -1 else 'white'
    canvas.create_oval(pixelX - pointsize, pixelY - pointsize, pixelX + pointsize, pixelY + pointsize, fill=color) 


for i in range(100):
    for data in trainingData:
        points = [data.x, data.y]
        perceptron.Train(points, data.label)

canvas.mainloop()