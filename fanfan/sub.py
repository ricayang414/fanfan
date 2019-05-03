import tkinter
from main import *
from tkinter import *
from tkinter import font
from tkinter import filedialog
from PIL import Image, ImageTk
import userInformation

class sub(Frame):
    def __init__(self, cvs, username, master = None):
        Frame.__init__(self, master, bg = "AntiqueWhite")
        self.cvs = cvs
        self.username = username
        self.root = master
        self.createPage()

    def createPage(self):
        f = font.Font(size = 20, family = "Times")

        Label_fillup = []
        for i in range(0,3):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[i].pack()

        L1 = Label(self, text = "hello " + self.username + "! you are almost done", font = f, bg = "AntiqueWhite")
        L1.pack()

        self.photoName = StringVar()

        B1 = Button(self, text = "select your profile photo", command = self.selectFileName, bg = "WhiteSmoke")
        B1.pack()

    def selectFileName(self):
        selectFile = filedialog.askopenfilename(title = "select your profile photo")
        self.photoName.set(selectFile)
        load = Image.open(selectFile)

        w_box = 200
        h_box = 200

        load = self.resize(w_box, h_box, load)

        render = ImageTk.PhotoImage(load)

        img = Label(self, image = render)
        img.image = render
        img.pack()

        b2 = Button(self, text = "finish signup!", command = self.nextCallBack)
        b2.pack()

    def resize(self, w_box, h_box, image):
        w, h = image.size
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h

        factor = min([f1,f2])

        width = int(w*factor)
        height = int(h*factor)

        return image.resize((width,height), Image.ANTIALIAS)

    def nextCallBack(self):
        self.destroy()
        userInformation.writePhotoInfo(self.username, self.photoName.get())
        Frame_main = main(self.cvs, self.username, self.root)
        self.cvs.create_window(500, 215, width = 500, height = 430, window = Frame_main)