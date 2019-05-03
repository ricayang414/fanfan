import userInformation
import tkinter
from tkinter import *
from tkinter import ttk # combo box
from sub import *
from tkinter import font
from dateSelection import *
# Frame defined by Tkinter
class signupFirst(Frame):
    def __init__(self, cvs, master = None):
        Frame.__init__(self,master,bg = "AntiqueWhite")
        self.root = master
        self.cvs = cvs

        # string var for username
        self.userNameVar = StringVar()

        # string var for password
        self.passwordVar = StringVar()

        # start the signup page
        self.createPage()

    def createPage(self):
        font_label_fg = font.Font(size=12, family="Times")

        Label_fillup = []
        for i in range(0,5):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[i].pack()

        # set the label and entry for username
        Label_username = Label(self, text = "Please enter your user name", bg = "AntiqueWhite", font = font_label_fg)
        Entry_username = Entry(self, textvariable = self.userNameVar, bg = "AliceBlue")
        Label_username.pack()
        Entry_username.pack()

        # set the label and entry for password
        Label_password = Label(self, text = "please enter your password", bg = "AntiqueWhite", font = font_label_fg)
        Entry_password = Entry(self, textvariable = self.passwordVar, bg = "AliceBlue", show = "*")
        Label_password.pack()
        Entry_password.pack()


        Frame_buttons = Frame(self, bg = "AntiqueWhite")
        Frame_buttons.pack()
        Button_prev = Button(Frame_buttons, text = "Back", bg = "WhiteSmoke", command = self.backCallBack)
        Button_prev.pack(side = LEFT)

        Label_fillup = []
        for i in range(0,2):
            Label_fillup.append(Label(Frame_buttons, width = 8, bg = "AntiqueWhite"))
            Label_fillup[i].pack(side = LEFT)

        Button_next = Button(Frame_buttons, text = "Next", bg = "WhiteSmoke", command = self.nextCallBack)
        Button_next.pack(side = RIGHT)

    def nextCallBack(self):
        self.destroy()
        Frame_signup_second = signupSecond(self.cvs, [self.userNameVar.get(), self.passwordVar.get()], self.root)
        self.cvs.create_window(500,215,width = 500,height = 430, window = Frame_signup_second)

    def backCallBack(self):
        self.destroy()
        Frame_login = login(self.cvs, self.root)
        self.cvs.create_window(500, 215, width = 500, height = 300, window = Frame_login)

class signupSecond(Frame):
    def __init__(self,cvs,userInfo,master = None):
        Frame.__init__(self,master, bg = "AntiqueWhite")

        self.cvs= cvs
        self.userInfo = userInfo
        self.root = master

        # string var for age selection
        self.age = StringVar()

        # int var for gender selection
        self.genderVar = IntVar()

        # string var for job selection
        self.jobs = StringVar()

        # list of topics and a list of int var for topic selection
        self.listTopic = ["makeup", "anime", "sports", "music", "art", "movie", "cooking", "car", "programming", "game", "pets"]
        self.checkVar_topic = []

        self.createFrame()

    def createFrame(self):
        font_label_fg = font.Font(size = 12, family = "Times")

        Label_fillup_verticle = []
        for i in range(0, 3):
            Label_fillup_verticle.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup_verticle[i].pack()

        # set label and entry for age
        Button_age = Button(self, text = "Please select your birthday", font = font_label_fg, bg = "WhiteSmoke", command = self.birthdayCallback)
        Button_age.pack()

        # set label and radiobutton for gender
        Label_gender = Label(self, text = "Please select your gender", font = font_label_fg, bg = "AntiqueWhite").pack()

        tempFrame3 = Frame(self)
        tempFrame3.pack()

        Radiobutton_gender1 = Radiobutton(tempFrame3, text = "male", value = 0, variable = self.genderVar, bg = "AntiqueWhite").grid(row = 1, column = 1)
        Radiobutton_gender2 = Radiobutton(tempFrame3, text = "female", value = 1, variable = self.genderVar, bg = "AntiqueWhite").grid(row = 1, column = 2)

        # set the label and combobox for job selection
        Label_job = Label(self, text = "please select your job", font = font_label_fg, bg = 'AntiqueWhite')
        combox = ttk.Combobox(self, textvariable = self.jobs)
        combox["values"] = ("students","artists","business/management","engineering/programming","politics", "education", "currently unemployed")
        combox["state"] = "readonly"
        Label_job.pack()
        combox.pack()

        # set the label for topic selection
        Label_topic = Label(self, text = "select topics you are interested in", font = font_label_fg, bg = "AntiqueWhite")
        Label_topic.pack()

        # set a separate frame to put topics in
        tempFrame = Frame(self, bg = "AntiqueWhite")
        tempFrame.pack()
        # set possible topics
        checkButtons_topic = []
        for i in range(0,4):
            self.checkVar_topic.append(IntVar())
            checkButtons_topic.append(Checkbutton(tempFrame, text = self.listTopic[i], variable = self.checkVar_topic[i], bg = "AntiqueWhite"))
            checkButtons_topic[i].grid(row = 1, column = i, sticky = tkinter.W)
        for i in range(4,8):
            self.checkVar_topic.append(IntVar())
            checkButtons_topic.append(Checkbutton(tempFrame, text = self.listTopic[i], variable = self.checkVar_topic[i], bg = "AntiqueWhite"))
            checkButtons_topic[i].grid(row = 2, column = i - 4, sticky = tkinter.W)
        for i in range(8,11):
            self.checkVar_topic.append(IntVar())
            checkButtons_topic.append(Checkbutton(tempFrame, text = self.listTopic[i], variable = self.checkVar_topic[i], bg = "AntiqueWhite"))
            checkButtons_topic[i].grid(row = 3, column = i - 8, sticky = tkinter.W)

        Frame_buttons = Frame(self, bg = "AntiqueWhite")
        Frame_buttons.pack()
        Button_prev = Button(Frame_buttons, text = "Back", bg = "WhiteSmoke", command = self.backCallback)
        Button_prev.pack(side = LEFT)

        Label_fillup = []
        for i in range(0,3):
            Label_fillup.append(Label(Frame_buttons, width = 8, bg = "AntiqueWhite"))
            Label_fillup[i].pack(side = LEFT)

        Button_next = Button(Frame_buttons, text = "Next", bg = "WhiteSmoke", command = self.nextCallback)
        Button_next.pack(side = RIGHT)

    def birthdayCallback(self):
        birthday_selection = tkinter.Toplevel()
        birthday_selection.geometry('220x220')
        birthday_selection['background'] = "AntiqueWhite"
        birthday_selection.resizable(0,0)
        timeSelection(birthday_selection)

    def backCallback(self):
        self.destroy()
        Frame_signup_first = signupFirst(self.cvs, self.root)
        self.cvs.create_window(500, 215, width = 500, height = 430, window = Frame_signup_first)

    def nextCallback(self):
        # transfer topic selection into a list
        topicSelection = []
        topic = []
        for i in self.checkVar_topic:
            value = True if i.get() == 1 else False
            topicSelection.append(value)

        for i in range(0, len(topicSelection)):
            if topicSelection[i]:
                topic.append(self.listTopic[i])

        # add age into userInfo
        info = ""
        with open("./Info/temp.txt", 'r') as temp_file:
            info = temp_file.read().replace("\n", "")
            info = info.split(";")

        self.userInfo.append(info[1])

        # transfer gender selection to either male or female
        gender = "male" if self.genderVar.get() == 0 else "female"
        self.userInfo.append(gender)

        # add user preferred topics into userInfo
        self.userInfo.append(topic)

        # add job into userInfo
        self.userInfo.append(self.jobs.get())

        self.destroy()
        Frame_signup_third = signupThird(self.cvs, self.userInfo, self.root)
        self.cvs.create_window(500, 215, width = 500, height = 430, window = Frame_signup_third)

class signupThird(Frame):
    def __init__(self,cvs,userInfo,master = None):
        Frame.__init__(self, master, bg = "AntiqueWhite")
        self.cvs = cvs
        self.userInfo = userInfo
        self.root = master

        # string var for price range selection
        self.lowerVar = StringVar()
        self.upperVar = StringVar()

        # list of tastes and a list of int var for taste selection
        self.list_taste = ["Thailand", "Chinese", "Fast", "American", "Japanese", "Sea", "Italian",
                           "Desert", "Korean", "Mexican", "Vietnam", "Peru", "African", "Vegetarian"]
        self.checkVar_taste = []

        # string var for facebook
        self.facebookVar = StringVar()

        self.createFrame()

    def createFrame(self):
        font_label_fg = font.Font(size=12, family="Times")

        Label_fillup_verticle = []
        for i in range(0, 3):
            Label_fillup_verticle.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup_verticle[i].pack()

        Label_taste = Label(self, text = "please select your preferred food style", font = font_label_fg, bg = "AntiqueWhite").pack()

        tempFrame2 = Frame(self, bg = "AntiqueWhite")
        tempFrame2.pack()

        checkButtons_taste = []
        for i in range(0, 3):
            self.checkVar_taste.append(IntVar())
            checkButtons_taste.append(Checkbutton(tempFrame2, text = self.list_taste[i], variable = self.checkVar_taste[i], bg = "AntiqueWhite"))
            checkButtons_taste[i].grid(row = 1, column = i, sticky = tkinter.W)
        for i in range(3, 6):
            self.checkVar_taste.append(IntVar())
            checkButtons_taste.append(Checkbutton(tempFrame2, text = self.list_taste[i], variable = self.checkVar_taste[i], bg = "AntiqueWhite"))
            checkButtons_taste[i].grid(row = 2, column = i - 3, sticky = tkinter.W)
        for i in range(6, 9):
            self.checkVar_taste.append(IntVar())
            checkButtons_taste.append(Checkbutton(tempFrame2, text = self.list_taste[i], variable = self.checkVar_taste[i], bg = "AntiqueWhite"))
            checkButtons_taste[i].grid(row = 3, column = i - 6, sticky = tkinter.W)
        for i in range(9, 12):
            self.checkVar_taste.append(IntVar())
            checkButtons_taste.append(Checkbutton(tempFrame2, text = self.list_taste[i], variable = self.checkVar_taste[i], bg = "AntiqueWhite"))
            checkButtons_taste[i].grid(row = 4, column = i - 9, sticky = tkinter.W)
        for i in range(12, 14):
            self.checkVar_taste.append(IntVar())
            checkButtons_taste.append(Checkbutton(tempFrame2, text = self.list_taste[i], variable = self.checkVar_taste[i], bg = "AntiqueWhite"))
            checkButtons_taste[i].grid(row = 5, column = i - 12, sticky = tkinter.W)

        # set price range
        Label_price = Label(self, text = "please enter your preferred price range", font = font_label_fg, bg = "AntiqueWhite")
        Label_price.pack()
        tempFrame4 = Frame(self, bg = "AntiqueWhite")
        tempFrame4.pack()

        Entry_lower = Entry(tempFrame4, width = 6, textvariable = self.lowerVar, bg = "AliceBlue")
        Label_hash = Label(tempFrame4, text = "  to  ", bg = "AntiqueWhite")
        Entry_upper = Entry(tempFrame4, width = 6, textvariable = self.upperVar, bg = "AliceBlue")
        Entry_lower.grid(row = 0, column = 1)
        Label_hash.grid(row = 0, column = 2)
        Entry_upper.grid(row = 0, column = 3)

        # set facebook account connection
        Label_facebook = Label(self, text = "please enter your facebook account", bg = "AntiqueWhite", font = font_label_fg)
        Entry_facebook = Entry(self, textvariable = self.facebookVar, width = 20, bg = "AliceBlue")
        Label_facebook.pack()
        Entry_facebook.pack()


        Frame_buttons = Frame(self, bg = "AntiqueWhite")
        Frame_buttons.pack()
        Button_prev = Button(Frame_buttons, text = "Back", bg = "WhiteSmoke", command = self.backCallback)
        Button_prev.pack(side = LEFT)

        Label_fillup = []
        for i in range(0,2):
            Label_fillup.append(Label(Frame_buttons, width = 8, bg = "AntiqueWhite"))
            Label_fillup[i].pack(side = LEFT)

        Button_next = Button(Frame_buttons, text = "Next", bg = "WhiteSmoke", command = self.nextCallback)
        Button_next.pack(side = RIGHT)

    def backCallback(self):
        self.destroy()
        Frame_signup_second = signupSecond(self.cvs, self.root)
        self.cvs.create_window(500, 215, width = 500, height = 430, window = Frame_signup_second)

    def nextCallback(self):

        #transfer food preference to a list
        tasteSelection = []
        taste = []
        for i in self.checkVar_taste:
            value = True if i.get() == 1 else False
            tasteSelection.append(value)

        for i in range(0, len(tasteSelection)):
            if tasteSelection[i]:
                taste.append(self.list_taste[i])

        self.userInfo.append(taste)

        self.userInfo.append([self.lowerVar.get(), self.upperVar.get()])

        self.userInfo.append(self.facebookVar.get())

        with open('./Info/temp.txt', 'r+') as temp_file:
            info = temp_file.read().replace("\n", "")
            info = info.split(";")
            temp_file.truncate()
        self.userInfo.append(info[0])

        userInformation.writeUserInfo(self.userInfo)

        self.destroy()
        Frame_select_photo = sub(self.cvs, self.userInfo[0], self.root)
        self.cvs.create_window(500, 215, width = 500, height = 430, window = Frame_select_photo)

class login(Frame):
    def __init__(self, cvs, master = None):
        Frame.__init__(self,master, bg = "AntiqueWhite") # initializer background color= antique white
        self.root = master

        self.username = StringVar() # under the tk library
        self.password = StringVar()
        self.cvs = cvs

        self.createPage()

    def createPage(self):
        font_label_fg = font.Font(size=12, family="Times")

        Label_fillup = []
        for i in range(0,3):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[i].pack(anchor = CENTER) # anchor means put in the center of the upper level boundary.

        Label_username = Label(self, text = "please enter your username",bg = "AntiqueWhite", font = font_label_fg) # fg used to adjust the font color label used to display information without any more actinities on the information
        Entry_username = Entry(self, textvariable = self.username, bg = "AliceBlue")
        Label_username.pack()  # pack method to put it in the correct location
        Entry_username.pack()

        Label_password = Label(self, text = "please enter your password",bg = "AntiqueWhite", font = font_label_fg)
        Entry_password = Entry(self, textvariable = self.password, bg = "AliceBlue", show = "*")
        Label_password.pack()
        Entry_password.pack()

        Button_login = Button(self, text = "Login!", bg = "WhiteSmoke", command = self.loginCallBack)
        Button_login.pack()

        Button_signup = Button(self, text = "Signup a new account!", bg = "WhiteSmoke", command = self.signupCallBack)
        Button_signup.pack()

        self.Label_alert = Label(self, text = "username or password wrong", fg = "red", bg = "AntiqueWhite")

    def loginCallBack(self):
        self.Label_alert.pack_forget()
        result = userInformation.checkPassword(self.username.get(), self.password.get())
        if result:
            self.destroy() # if is legal for password and username, the current page will destroy itself and go into the next page.
            Frame_home = main(self.cvs, self.username.get(), self.root)
            self.cvs.create_window(500, 215, width = 500, height = 430, window = Frame_home) # create a new window on the same canvas to show user's homepage.
        else:
            self.Label_alert.pack()

    def signupCallBack(self):
        self.destroy()
        Frame_signup = signupFirst(self.cvs,self.root)
        self.cvs.create_window(500, 215, width = 500, height = 430, window = Frame_signup)
