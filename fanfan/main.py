import tkinter
import restaurant
import userInformation
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import selectRestaurant
from tkinter import messagebox
from frames import *
from time import ctime


class main(Frame):
    def __init__(self, cvs, username, master = None):
        Frame.__init__(self, master, bg = "AntiqueWhite")
        self.cvs = cvs
        self.root = master
        self.imageAddress = userInformation.getPhotoInfo(username)
        self.username = username

        menu = Menu(self.root)

        # add sub menu within topbar
        subMenu1 = Menu(self.root)
        subMenu1.add_command(label = "edit preference", command = self.editPreference)
        subMenu1.add_command(label = "edit personal information")

        self.Frame_main = mainFrame(self.cvs, self.username, master)

        self.cvs.create_window(500, 215, width=500, height=430, window=self.Frame_main)

    def editPreference(self):
        preferencePage = Toplevel()
        preferencePage.geometry('600x300')
        editPreferenceFrame = editPreference(self.username, preferencePage)
        editPreferenceFrame.pack()

    def bCallBack(self):
        print(self.username)

    def resize(self, w_box, h_box, image):
        w, h = image.size
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h

        factor = min([f1,f2])

        width = int(w*factor)
        height = int(h*factor)

        return image.resize((width,height), Image.ANTIALIAS)
