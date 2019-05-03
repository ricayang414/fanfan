import userInformation
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
import appointmentInfo

class appointmentInfoMain(Frame):
    def __init__(self, cvs, username, master = None):
        Frame.__init__(self, master)
        self.cvs = cvs
        self.username = username
