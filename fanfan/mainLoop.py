import tkinter
from tkinter import *
from PIL import Image, ImageTk
from signup import *

root = tkinter.Tk() # create the window

root.title("fanfan")
root.geometry('1000x430')
root.resizable(0,0)

imageName = Image.open('./background.jpg')
im = ImageTk.PhotoImage(imageName)


Canvas_bg1 = Canvas(root,bg = 'HotPink',width = 1000, height = 500)
Canvas_bg1.pack(side = LEFT)
Canvas_bg1.create_image(500,215,image = im) # in the center of the canvas with the 500*215 coordinate.

a = login(Canvas_bg1,root)

login_frame = Canvas_bg1.create_window(500,215,width = 500,height = 300, window = a)

root.mainloop()

