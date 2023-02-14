#Import the required library
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry
win.geometry("750x280")

#Create a canvas object
canvas= Canvas(win, width= 1000, height= 750, bg="Black")
def my_func():
    print("This code is created by C.D")
#Add a text in Canvas
canvas.create_text(600, 50, text="*** HAR HAR MAHADEV *** ", fill="white")
canvas.create_text(600, 20, text="______ Creator : Chandrika Dhale ", fill="white")

canvas.pack()

win.mainloop()