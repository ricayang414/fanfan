import tkinter
import userInformation
from tkinter import *
from PIL import Image, ImageTk
import selectRestaurant
from tkinter import messagebox
from main import *
from tkinter import ttk
import time
import timeInfo
import appointmentInfo
from tkinter import font

class makeAppointment(Frame):
    def __init__(self, cvs, username, master=None):
        Frame.__init__(self, master, bg = "AntiqueWhite")
        self.cvs = cvs
        self.root = master
        self.username = username

        self.genderPreference = IntVar()
        self.ageLowerBound = StringVar()
        self.ageUpperBound = StringVar()

        self.monthVar = StringVar()
        self.dayVar = StringVar()
        self.yearVar = StringVar()

        self.year = int(time.strftime("%Y", time.localtime()))
        self.month = int(time.strftime("%m", time.localtime()))
        self.day = int(time.strftime("%d", time.localtime()))
        self.date = timeInfo.calculateDate(self.year, self.month, self.day, 60)

        self.mealVar = IntVar()
        self.lunchTimeSpan = []
        self.dinnerTimeSpan = []

        self.lunchTimes = ["11:00-11:30", "11:30-12:00", "12:00-12:30", "12:30-1:00", "1:00-1:30", "1:30-2:00"]
        self.dinnerTimes = ["5:00-5:30", "5:30-6:00", "6:00-6:30", "6:30-7:00", "7:00-7:30", "7:30-8:00"]

        self.createNewPage()

    def createNewPage(self):
        font_label = font.Font(size = 13, family = "Arial")

        image_left = Image.open('./left.jpg')
        image_left = self.resize(20,20,image_left)
        render_left = ImageTk.PhotoImage(image_left)



        Label_fillup = []
        for i in range(0,2):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[-1].pack()

        Button_back = Button(self, image = render_left, command = self.backCallback)
        Button_back.image = render_left
        Button_back.pack(anchor = NW)

        for i in range(0,2):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[-1].pack()

        # set up gender preference
        Label_gender = Label(self, text="select your gender preference", bg = "AntiqueWhite", font = font_label, fg = "MidnightBlue")
        Label_gender.pack()

        Frame_gender = Frame(self, bg = "AntiqueWhite")
        Frame_gender.pack()

        Radio_gender1 = Radiobutton(Frame_gender, text="male", value=0, variable=self.genderPreference, bg = "AntiqueWhite")
        Radio_gender2 = Radiobutton(Frame_gender, text="female", value=1, variable=self.genderPreference, bg = "AntiqueWhite")
        Radio_gender3 = Radiobutton(Frame_gender, text="no preference", value=2, variable=self.genderPreference, bg = "AntiqueWhite")
        Radio_gender1.grid(row = 0, column = 1)
        Radio_gender2.grid(row = 0, column = 2)
        Radio_gender3.grid(row = 0, column = 3)

        # set up age preference
        Label_age = Label(self, text="select your age preference", bg = "AntiqueWhite", font = font_label, fg = "MidnightBlue")
        Label_age.pack()

        Frame_age = Frame(self, bg = "AntiqueWhite")
        Frame_age.pack()
        Entry_ageLowerBound = Entry(Frame_age, textvariable=self.ageLowerBound, bg = "AliceBlue")
        Entry_ageUpperBound = Entry(Frame_age, textvariable=self.ageUpperBound, bg = "AliceBlue")
        Label_hash = Label(Frame_age, text=" to ", bg = "AntiqueWhite")

        Entry_ageLowerBound.grid(row=1, column=2)
        Label_hash.grid(row=1, column=3)
        Entry_ageUpperBound.grid(row=1, column=4)

        # set up time selection

        Label_timeSelectionNote = Label(self, text = "Please select your preferred time range on the following", bg = "AntiqueWhite", font = font_label, fg = "MidnightBlue")
        Label_timeSelectionNote.pack()

        Frame_time_selection = Frame(self)
        Frame_time_selection.pack()

        Label_yearSelection = Label(Frame_time_selection, text = "year", bg = "AntiqueWhite")
        Label_yearSelection.grid(row = 1, column = 1)
        Combo_yearSelection = ttk.Combobox(Frame_time_selection, textvariable = self.yearVar)
        Combo_yearSelection['values'] = tuple(range(self.year, self.date[0] + 1))
        Combo_yearSelection['state'] = 'readonly'
        Combo_yearSelection.grid(row = 1, column = 2)


        Label_monthSelection = Label(Frame_time_selection, text = "month", bg = "AntiqueWhite")
        Label_monthSelection.grid(row = 1, column = 3)
        self.Combo_monthSelection = ttk.Combobox(Frame_time_selection, textvariable = self.monthVar)
        self.Combo_monthSelection['state'] = 'readonly'
        self.Combo_monthSelection.grid(row = 1, column = 4)

        Combo_yearSelection.bind('<<ComboboxSelected>>', self.yearSelected)

        Label_daySelection = Label(Frame_time_selection,text = "date", bg = "AntiqueWhite")
        Label_daySelection.grid(row = 1, column = 5)
        self.Combo_daySelection = ttk.Combobox(Frame_time_selection, textvariable = self.dayVar)
        self.Combo_daySelection['state'] = 'readonly'
        self.Combo_daySelection.grid(row = 1, column = 6)

        self.Combo_monthSelection.bind('<<ComboboxSelected>>', self.monthComboSelected)

        Label_mealSelection = Label(self, text = "please select dinner or lunch", bg = "AntiqueWhite", font = font_label, fg = "MidnightBlue")
        Label_mealSelection.pack()

        Frame_meal_selection = Frame(self, bg = "AntiqueWhite")
        Frame_meal_selection.pack()

        for i in range(1,3):
            Label_fillup.append(Label(Frame_meal_selection, bg = "AntiqueWhite"))
            Label_fillup[-1].grid(row = 1, column = i)

        Radiobutton_mealSelection1 = Radiobutton(Frame_meal_selection, text = "lunch", value = 0, variable = self.mealVar, command = self.lunchCallBack, bg = "AntiqueWhite")
        Radiobutton_mealSelection2 = Radiobutton(Frame_meal_selection, text = "dinner", value = 1, variable = self.mealVar, command = self.dinnerCallBack, bg = "AntiqueWhite")

        Radiobutton_mealSelection1.grid(row = 1, column = 4)
        Radiobutton_mealSelection2.grid(row = 1, column = 5)

        self.lunchFrame = Frame(self, bg = "AntiqueWhite")
        self.checkButton_lunchSelection = []
        for i in range(0,3):
            self.lunchTimeSpan.append(IntVar())
            self.checkButton_lunchSelection.append(Checkbutton(self.lunchFrame, text = self.lunchTimes[i], width = 10, variable = self.lunchTimeSpan[i], bg = "AntiqueWhite"))
            self.checkButton_lunchSelection[i].grid(row = 1, column = i + 1)
        for i in range(3,6):
            self.lunchTimeSpan.append(IntVar())
            self.checkButton_lunchSelection.append(Checkbutton(self.lunchFrame, text = self.lunchTimes[i], width = 10, variable = self.lunchTimeSpan[i], bg = "AntiqueWhite"))
            self.checkButton_lunchSelection[i].grid(row = 2, column = i - 2)

        self.dinnerFrame = Frame(self, bg = "AntiqueWhite")
        self.checkButton_dinnerSelection = []
        for i in range(0,3):
            self.dinnerTimeSpan.append(IntVar())
            self.checkButton_dinnerSelection.append(Checkbutton(self.dinnerFrame, text = self.dinnerTimes[i], width = 10, variable = self.dinnerTimeSpan[i], bg = "AntiqueWhite"))
            self.checkButton_dinnerSelection[i].grid(row = 1, column = i + 1)
        for i in range(3,6):
            self.dinnerTimeSpan.append(IntVar())
            self.checkButton_dinnerSelection.append(Checkbutton(self.dinnerFrame, text = self.dinnerTimes[i], width = 10, variable = self.dinnerTimeSpan[i], bg = "AntiqueWhite"))
            self.checkButton_dinnerSelection[i].grid(row = 2, column = i - 2)

        # set up confirm button
        self.Button_confirm = Button(self, text="Confirm!", command=self.confirmCallBack)

    def backCallback(self):
        self.destroy()
        Frame_main = mainFrame(self.cvs, self.username, self.root)
        self.cvs.create_window(500, 215, width=500, height=430, window=Frame_main)

    def lunchCallBack(self):
        self.dinnerFrame.pack_forget()
        self.Button_confirm.pack_forget()

        whichMonth = "0" + self.monthVar.get() if len(self.monthVar.get()) == 1 else self.monthVar.get()
        whichDay = "0" + self.dayVar.get() if len(self.dayVar.get()) == 1 else self.dayVar.get()
        dateResult = self.yearVar.get() + whichMonth + whichDay

        if not appointmentInfo.isExist(self.username, dateResult):
            for i in range(0, len(self.checkButton_lunchSelection)):
                self.checkButton_lunchSelection[i]['state'] = 'active'
            self.lunchFrame.pack()
            self.Button_confirm.pack()
        else:
            for i in range(0, len(self.checkButton_lunchSelection)):
                self.checkButton_lunchSelection[i]["state"] = 'disable'
            self.lunchFrame.pack()

    def dinnerCallBack(self):
        self.lunchFrame.pack_forget()
        self.Button_confirm.pack_forget()

        whichMonth = "0" + self.monthVar.get() if len(self.monthVar.get()) == 1 else self.monthVar.get()
        whichDay = "0" + self.dayVar.get() if len(self.dayVar.get()) == 1 else self.dayVar.get()
        dateResult = self.yearVar.get() + whichMonth + whichDay

        if not appointmentInfo.isExist(self.username, dateResult):
            for i in range(0,len(self.checkButton_dinnerSelection)):
                self.checkButton_dinnerSelection[i]['state'] = 'active'
            self.dinnerFrame.pack()
            self.Button_confirm.pack()
        else:
            for i in range(0, len(self.checkButton_dinnerSelection)):
                self.checkButton_dinnerSelection[i]["state"] = 'disable'
            self.dinnerFrame.pack()


    def confirmCallBack(self):

        userInfo = userInformation.searchUserInfo(self.username)
        users = userInformation.readUserInfo()

        preferenceInfo = []
        preferenceInfo.append(self.username)
        preferenceInfo.append(self.genderPreference.get())
        preferenceInfo.append([self.ageLowerBound.get(), self.ageUpperBound.get()])
        preferenceInfo.append(userInfo[6])
        preferenceInfo.append(userInfo[7])
        preferenceInfo.append(userInfo[4])
        preferenceInfo.append(userInfo[5])

        whichMonth = "0" + self.monthVar.get() if len(self.monthVar.get()) == 1 else self.monthVar.get()
        whichDay = "0" + self.dayVar.get() if len(self.dayVar.get()) == 1 else self.dayVar.get()
        dateResult = self.yearVar.get() + whichMonth + whichDay
        timeResult = []
        if self.mealVar.get() == 0:
            for i in range(0, len(self.lunchTimeSpan)):
                if self.lunchTimeSpan[i].get() == 1:
                    if not appointmentInfo.isExist(self.username, self.date):
                        timeResult.append(self.lunchTimes[i])
        else:
            for i in range(0, len(self.dinnerTimeSpan)):
                if self.dinnerTimeSpan[i].get() == 1:
                    if not appointmentInfo.isExist(self.username, self.date):
                        timeResult.append(self.dinnerTimes[i])

        whichMeal = "lunch" if self.mealVar.get() == 0 else "dinner"

        for i in timeResult:
            dateAndTimeResult = [self.username, [dateResult, whichMeal, i]]
            timeInfo.writeTimeInfo(dateAndTimeResult)

        result = selectRestaurant.selectRestaurant(preferenceInfo, users)

        if result:
            self.matchResult = result
            print(self.matchResult)
            callBack = tkinter.messagebox.askyesno("We got a match for you!", "you got a match with " + self.matchResult[0] + " at " + self.matchResult[1][0])
            self.destroy()
            Frame_main = mainFrame(self.cvs, self.username, self.root)
            self.cvs.create_window(500, 215, width=500, height=430, window = Frame_main)

        else:
            tkinter.messagebox.showinfo("sorry!", "cannot find a match for you right now\nmaybe try again later!")
            self.destroy()
            Frame_main = mainFrame(self.cvs, self.username, self.root)
            self.cvs.create_window(500, 215, width=500, height=430, window = Frame_main)

    def yearSelected(self,a):
        if self.year == self.date[0]:
            self.Combo_monthSelection['values'] = tuple(range(self.month, self.date[1] + 1))
        else:
            months = timeInfo.generateMonthRangeAcrossYear(self.month, self.date[1])
            difference = 12 - self.month + 1
            print(difference)
            if self.year == int(self.yearVar.get()):
                self.Combo_monthSelection['values'] = tuple(months[:difference])
            else:
                self.Combo_monthSelection['values'] = tuple(months[difference:])

    def monthComboSelected(self,a):
        if self.date[1] < self.month:
            if self.monthVar.get() == str(self.month):
                self.Combo_daySelection['values'] = timeInfo.generateDateRangeToEndOfMonth(self.year, self.month, self.day)
            elif int(self.monthVar.get()) > self.month:
                self.Combo_daySelection['values'] = timeInfo.generateDateRangeToEndOfMonth(self.year, int(self.monthVar.get()), 1)
            elif int(self.monthVar.get()) < self.date[1]:
                self.Combo_daySelection['values'] = timeInfo.generateDateRangeToEndOfMonth(self.date[0],int(self.monthVar.get()), 1)
            else:
                self.Combo_daySelection['values'] = tuple(range(1, self.date[2] + 1))
        else:
            if int(self.monthVar.get()) == self.month:
                self.Combo_daySelection['values'] = timeInfo.generateDateRangeToEndOfMonth(self.year, self.month, self.day)

            elif int(self.monthVar.get()) < range(self.month, self.date[1] + 1)[-1]:
                self.Combo_daySelection['values'] = timeInfo.generateDateRangeToEndOfMonth(self.year, int(self.monthVar.get()), 1)

            else:
                self.Combo_daySelection['values'] = tuple(range(1, self.date[2] + 1))

    def resize(self, w_box, h_box, image):
        w, h = image.size
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h

        factor = min([f1,f2])

        width = int(w*factor)
        height = int(h*factor)

        return image.resize((width,height), Image.ANTIALIAS)

class mainFrame(Frame):
    def __init__(self, cvs, username, master = None):
        Frame.__init__(self,master, bg = "AntiqueWhite")
        self.cvs = cvs
        self.root = master
        self.username = username

        self.imageAddress = userInformation.getPhotoInfo(self.username)

        self.userInfo = userInformation.searchUserInfo(self.username)


        self.editMainPage = Toplevel()
        self.editMainPage.geometry('300x400')
        self.editMainPage.resizable(0,0)
        self.editMainPage['bg'] = "AntiqueWhite"
        self.editMainPage.protocol("WM_DELETE_WINDOW", self.on_closing_setting)
        self.editMainPage.withdraw()

        self.createFrame()

    def createFrame(self):

        Label_fillup = []

        font_Label = font.Font(family = 'Arial', size = 13)
        f = font.Font(family = 'Arial', size = 15)
        font_Label_appointment = font.Font(family = 'Arial', size = 11)

        for i in range(0,1):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[-1].pack()

        Frame_userInformation = Frame(self, bg = "AntiqueWhite")
        Frame_userInformation.pack(anchor = NW)

        # set space for left side and between Frame_userinformation and Label_appointment
        for i in range(0,2):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[-1].pack()
        for i in range(0,2):
            Label_fillup.append(Label(Frame_userInformation, bg = "AntiqueWhite", width = 2))
            Label_fillup[-1].grid(row = 0, column = i)

        load = Image.open(self.imageAddress)
        w_box = 100
        h_box = 100
        load = self.resize(w_box, h_box, load)
        render = ImageTk.PhotoImage(load)
        img = Label(Frame_userInformation, image=render)
        img.image = render
        img.grid(row = 0, column = 2)

        load_setting = Image.open('./settings.jpg')
        w_box_setting = 30
        h_box_setting = 30
        load_setting = self.resize(w_box_setting, h_box_setting, load_setting)
        render_setting = ImageTk.PhotoImage(load_setting)

        Frame_username_facebook = Frame(Frame_userInformation, bg = "AntiqueWhite")
        Frame_username_facebook.grid(row = 0, column = 3, sticky = tkinter.N)
        self.Lable_username = Label(Frame_username_facebook, text = self.username, bg = "AntiqueWhite", font = font_Label)
        self.Lable_username.grid(row = 0, column = 0, sticky = tkinter.W)
        Label_facebook = Label(Frame_username_facebook, text = self.userInfo[8], bg = "AntiqueWhite", font = font_Label)
        Label_facebook.grid(row = 1, column = 0, sticky = tkinter.W)


        self.Button_setting = Button(Frame_username_facebook, image = render_setting, command = self.settingCallback)
        self.Button_setting.image = render_setting
        self.Button_setting.grid(row = 0, column = 1)

        image_plus = Image.open('./plus.jpg')
        image_plus = self.resize(20,20,image_plus)
        render_plus = ImageTk.PhotoImage(image_plus)

        Frame_appointment = Frame(self, bg = "AntiqueWhite")
        Frame_appointment.pack()
        Label_appointment = Label(Frame_appointment, text = "Here are your appointments!", bg = 'AntiqueWhite', font = f, fg = "NavyBlue")
        Label_appointment.pack(side = LEFT)

        # set up button for more information
        Button_moreinfo = Button(Frame_appointment, image = render_plus)
        Button_moreinfo.image = render_plus
        Button_moreinfo.pack(side = LEFT)

        appointments = appointmentInfo.getAppointment(self.username)
        appointmentFrame = Frame(self, bg = 'AntiqueWhite')
        appointmentFrame.pack()

        counter = 0
        Label_appointmentInfo = []

        if len(appointments) != 0:
            for i in appointments:
                if counter >= 3:
                    break
                information = appointmentInfo.listToDateInfo(i[1])
                Label_appointmentInfo.append(Label(appointmentFrame, text = "with " + i[0] + " at " + i[2] + " on " + information, bg = 'AntiqueWhite', width = 50,
                                                   font = font_Label_appointment))
                Label_appointmentInfo[counter].grid(row = counter, column = 1)
                counter += 1
        else:
            Label_alertInfo = Label(appointmentFrame, text = "Sorry... you currently have no appointment", bg = 'AntiqueWhite', width = 50)
            Label_alertInfo.grid(row = 0, column = 1)

        while counter < 3:
            Label_fillup.append(Label(appointmentFrame, bg = "AntiqueWhite"))
            Label_fillup[-1].grid(row = counter, column = 1)
            counter += 1

        self.B_makeAppointment = Button(self, text = "Make appointment!", command = self.makeAppointmentCallBack)
        self.B_makeAppointment.pack()

    def makeAppointmentCallBack(self):
        self.destroy()
        self.Frame_appointment = makeAppointment(self.cvs, self.username, self.root)
        self.cvs.create_window(500, 215, width=550, height=500, window=self.Frame_appointment)

    def resize(self, w_box, h_box, image):
        w, h = image.size
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h

        factor = min([f1,f2])

        width = int(w*factor)
        height = int(h*factor)

        return image.resize((width,height), Image.ANTIALIAS)

    def settingCallback(self):
        print(self.username)

        self.Button_setting['state'] = "disable"
        self.B_makeAppointment['state'] = 'disable'

        self.editMainPage.deiconify()
        info_main = editInfoMain(self.username, self.Button_setting, self.B_makeAppointment, self.editMainPage)
        info_main.pack()

    def on_closing_setting(self):
        self.Button_setting['state'] = 'normal'
        self.B_makeAppointment['state'] = 'normal'

        file = open('./Info/temp.txt', 'r+')
        temp = file.read()
        if temp != "":
            self.username = file.read()
            self.Lable_username['text'] = self.username

        file.truncate()
        file.close()

        self.editMainPage.withdraw()

class editPreference(Frame):
    def __init__(self, username, master = None):
        Frame.__init__(self, master, bg = "AntiqueWhite")

        self.root = master
        self.username = username

        self.userInfo = userInformation.searchUserInfo(self.username)
        self.tasteVar = []
        self.tastes = ["Thailand", "Chinese", "Fast", "American", "Japanese", "Sea", "Italian",
                           "Desert", "Korean", "Mexican", "Vietnam", "Peru", "African", "Vegetarian"]

        self.lowerPrice = StringVar()
        self.upperPrice = StringVar()

        self.createNewFrame()

    def createNewFrame(self):
        self.tastePref_ori = self.userInfo[6]
        self.priceRange_ori = self.userInfo[7]

        font_button = font.Font(size = 12, family = "Arial", weight = font.BOLD)
        f = font.Font(family = "Arial", size = 13)

        Label_fillup = []

        for i in range(0, 2):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[-1].pack()

        Label_taste = Label(self, text = "please select your taste preference", bg = 'AntiqueWhite', font = f)
        Label_taste.pack()

        Label_fillup.append(Label(self, bg = "AntiqueWhite"))
        Label_fillup[-1].pack()

        Frame_taste = Frame(self, bg = "AntiqueWhite")
        Frame_taste.pack()
        Checkbutton_taste = []
        for i in range(0, 7):
            self.tasteVar.append(IntVar())
            Checkbutton_taste.append(Checkbutton(Frame_taste, text = self.tastes[i], variable = self.tasteVar[i], bg = "AntiqueWhite"))
            Checkbutton_taste[i].grid(row = 1, column = i, sticky = tkinter.W)

        for i in range(7,14):
            self.tasteVar.append(IntVar())
            Checkbutton_taste.append(Checkbutton(Frame_taste, text = self.tastes[i], variable = self.tasteVar[i], bg = "AntiqueWhite"))
            Checkbutton_taste[i].grid(row = 2, column = i - 7, sticky = tkinter.W)

        # set space between checkbuttons and next label
        for i in range(0,2):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[-1].pack()

        # set taste preference to original
        for i in self.tastePref_ori:
            if i in self.tastes:
                j = self.tastes.index(i)
                self.tasteVar[j].set(1)

        Label_price = Label(self, text = "Please enter your preferred price range", bg = 'AntiqueWhite', font = f)
        Label_price.pack()

        Frame_price = Frame(self, bg = "AntiqueWhite")
        Frame_price.pack()
        for i in range(0,2):
            Label_fillup.append(Label(Frame_price, bg = "AntiqueWhite"))
            Label_fillup[-1].grid(row = 1, column = i)

        Entry_lowerprice = Entry(Frame_price, textvariable = self.lowerPrice, width = 8, bg = "AliceBlue")
        Entry_lowerprice.grid(row = 1, column = 2)

        Label_hash = Label(Frame_price, text = " to ", width = 5, bg = "AntiqueWhite")
        Label_hash.grid(row = 1, column = 3)

        Entry_upperprice = Entry(Frame_price, textvariable = self.upperPrice, width = 8, bg = "AliceBlue")
        Entry_upperprice.grid(row = 1, column = 4)

        self.lowerPrice.set(str(self.priceRange_ori[0]))
        self.upperPrice.set(str(self.priceRange_ori[1]))

        for i in range(0,2):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[-1].pack()

        Frame_accept_cancel = Frame(self, bg = "AntiqueWhite")
        Frame_accept_cancel.pack(side = LEFT, ipadx = 100)

        for i in range(0,2):
            Label_fillup.append(Label(Frame_accept_cancel, bg = "AntiqueWhite", width = 4))
            Label_fillup[-1].grid(row = 0, column = i)

        Button_accept = Button(Frame_accept_cancel, text = "Accept", bg = "Green", bd = 4, font = font_button, command = self.acceptCallBack)
        Button_accept.grid(row = 0, column = 3, ipadx = 5, ipady = 5)
        Button_cancel = Button(Frame_accept_cancel, text = "Cancel", bg = "Red", bd = 4, font = font_button, command = self.cancelCallback)
        Button_cancel.grid(row = 0, column = 4, ipadx = 5, ipady = 5)

    def acceptCallBack(self):
        tastePref_new = []
        for i in range(0,len(self.tasteVar)):
            if self.tasteVar[i].get() == 1:
                tastePref_new.append(self.tastes[i])

        tasteUpadate = True
        priceUpdate = True

        if tastePref_new != self.tastePref_ori:
            tasteUpadate = userInformation.updateUserTaste(self.username, tastePref_new)

        priceRange_new = [self.lowerPrice.get(), self.upperPrice.get()]

        if priceRange_new[0] != self.priceRange_ori[0] or priceRange_new[1] != self.priceRange_ori[1]:
            priceUpdate = userInformation.updatePriceRange(self.username, priceRange_new)

        if tasteUpadate and priceUpdate:
            callBack = tkinter.messagebox.showinfo("Information updated!", "We have successfully updated your information!")
            if not callBack:
                self.root.destory()
        else:
            callBack = tkinter.messagebox.showinfo("Something is wrong...", "Sorry we could not update your information, try again!")

    def cancelCallback(self):
        self.destroy()
        editInfoMain(self.username, self.root)

class editUserInfo(Frame):
    def __init__(self, username, master = None):
        Frame.__init__(self, master, bg = "AntiqueWhite")

        self.root = master
        self.username = username

        self.job_var = StringVar()

        self.new_username_var = StringVar()

        userInfo = userInformation.searchUserInfo(self.username)
        self.topic_ori = userInfo[4]

        self.topic_var = []
        self.listTopic = ["makeup", "anime", "sports", "music", "art", "movie", "cooking", "car", "programming", "game", "pets"]

        self.createNewFrame()


    def createNewFrame(self):

        Label_fillup = []
        for i in range(0,3):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[-1].pack()

        font_label = font.Font(size = 13, family = "Arial")
        font_button = font.Font(size = 12, family = "Arial", weight = font.BOLD)

        Label_job = Label(self, text = "Please select your job", bg = "AntiqueWhite", font = font_label)
        Label_job.pack()

        combox_job = ttk.Combobox(self, textvariable=self.job_var, width = 25)
        combox_job["values"] = ("students", "artists", "business/management", "engineering/programming", "politics", "education","currently unemployed")
        combox_job["state"] = "readonly"
        combox_job.pack()

        Label_fillup.append(Label(self, bg = "AntiqueWhite"))
        Label_fillup[-1].pack()

        Label_topics = Label(self, text = "Please select your favorite topics", bg = "AntiqueWhite", font = font_label)
        Label_topics.pack()

        Frame_topic = Frame(self, bg = "AntiqueWhite")
        Frame_topic.pack(anchor = W)

        # set up interested topics part
        checkButtons_topic = []
        for i in range(0,4):
            self.topic_var.append(IntVar())
            checkButtons_topic.append(Checkbutton(Frame_topic, text = self.listTopic[i], variable = self.topic_var[i], bg = "AntiqueWhite"))
            checkButtons_topic[i].grid(row = 1, column = i, sticky = tkinter.W)
        for i in range(4,8):
            self.topic_var.append(IntVar())
            checkButtons_topic.append(Checkbutton(Frame_topic, text = self.listTopic[i], variable = self.topic_var[i], bg = "AntiqueWhite"))
            checkButtons_topic[i].grid(row = 2, column = i - 4, sticky = tkinter.W)
        for i in range(8,11):
            self.topic_var.append(IntVar())
            checkButtons_topic.append(Checkbutton(Frame_topic, text = self.listTopic[i], variable = self.topic_var[i], bg = "AntiqueWhite"))
            checkButtons_topic[i].grid(row = 3, column = i - 8, sticky = tkinter.W)

        for i in range(0, 11):
            if self.listTopic[i] in self.topic_ori:
                self.topic_var[i].set(1)

        # set space between the two part
        for i in range(0,2):
            Label_fillup.append(Label(self, bg = "AntiqueWhite"))
            Label_fillup[-1].pack()

        # set accept and cancel frame
        Frame_accept_cancel = Frame(self, bg = "AntiqueWhite")
        Frame_accept_cancel.pack(anchor = NW, ipadx = 100)

        for i in range(0,2):
            Label_fillup.append(Label(Frame_accept_cancel, bg = "AntiqueWhite", width = 4))
            Label_fillup[-1].grid(row = 0, column = i)

        Button_accept = Button(Frame_accept_cancel, text = "Accept", bg = "Green", bd = 4, font = font_button, command = self.acceptCallback)
        Button_accept.grid(row = 0, column = 3, ipadx = 5, ipady = 5)
        Button_cancel = Button(Frame_accept_cancel, text = "Cancel", bg = "Red", bd = 4, font = font_button, command = self.cancelCallback)
        Button_cancel.grid(row = 0, column = 4, ipadx = 5, ipady = 5)

    def acceptCallback(self):
        # transfer topic selection into a list
        topicSelection = []
        topic = []
        for i in self.topic_var:
            value = True if i.get() == 1 else False
            topicSelection.append(value)

        for i in range(0, len(topicSelection)):
            if topicSelection[i]:
                topic.append(self.listTopic[i])

        if not len(topic) == 0 and not self.job_var.get() == "":
            userInformation.updateUserInfo(self.username, [topic, self.job_var.get()])
            messagebox.showinfo("Update success!", "Your information is successfully updated!")
        else:
            messagebox.showinfo("Sorry...", "Something wrong with your information, please try again")

        self.destroy()
        editInfoMain(self.username, self.root)

    def cancelCallback(self):
        self.destroy()
        editInfoMain(self.username, self.root)

class editPassword(Frame):
    def __init__(self, username, master = None):
        Frame.__init__(self, master, bg = "AntiqueWhite")

        self.username = username
        self.password = userInformation.searchUserInfo(self.username)[1]

        self.password_ori_var = StringVar()
        self.password_new_var = StringVar()
        self.password_sec_var = StringVar()

        self.createFrame()

    def createFrame(self):
        self.Label_fillup = []

        font_label = font.Font(family = "Arial", size = 13)
        font_button = font.Font(size = 12, family = "Arial", weight = font.BOLD)

        self.Label_fillup.append(Label(self, bg = "AntiqueWhite"))
        self.Label_fillup[-1].grid(row = 0, column = 0)

        Label_password_ori = Label(self, text = "Please enter your old password", bg = "AntiqueWhite", font = font_label)
        Label_password_ori.grid(row = 2, column = 0)

        Entry_password_ori = Entry(self, textvariable = self.password_ori_var, bg = "AliceBlue", width = 35, show = "*")
        Entry_password_ori.grid(row = 3, column = 0)

        self.Label_fillup.append(Label(self, bg = "AntiqueWhite"))
        self.Label_fillup[-1].grid(row = 4, column = 0)

        Label_password_new = Label(self, text = "Please enter your new password", bg = "AntiqueWhite", font = font_label)
        Label_password_new.grid(row = 5, column = 0)

        Entry_password_new = Entry(self, textvariable = self.password_new_var, bg = "AliceBlue", width = 35, show = "*")
        Entry_password_new.grid(row = 6, column = 0)

        self.Label_fillup.append(Label(self, bg = "AntiqueWhite"))
        self.Label_fillup[-1].grid(row = 7, column = 0)

        Label_password_sec = Label(self, text = "Please enter the new password again", bg = "AntiqueWhite", font = font_label)
        Label_password_sec.grid(row = 8, column = 0)

        Entry_password_sec = Entry(self, textvariable = self.password_sec_var, bg = "AliceBlue", width = 35, show = "*")
        Entry_password_sec.grid(row = 9, column = 0)

        self.Label_fillup.append(Label(self, bg = "AntiqueWhite", fg = "Red"))
        self.Label_fillup[-1].grid(row = 10, column = 0)

        Frame_accept_cancel = Frame(self, bg = "AntiqueWhite")
        Frame_accept_cancel.grid(row = 11, column = 0, sticky = tkinter.W)

        self.Label_fillup.append(Label(Frame_accept_cancel, bg = "AntiqueWhite", width = 7))
        self.Label_fillup[-1].grid(row = 0, column = 1)

        Button_accept = Button(Frame_accept_cancel, text = "Accept", bg = "Green", bd = 4, font = font_button, command = self.acceptCallback)
        Button_accept.grid(row = 0, column = 2, ipady = 5, ipadx = 5)
        Button_cancel = Button(Frame_accept_cancel, text = "Cancel", bg = "Red", bd = 4, font = font_button)
        Button_cancel.grid(row = 0, column = 3, ipady = 5, ipadx = 5)

    def acceptCallback(self):
        if not self.password == self.password_ori_var.get():
            self.Label_fillup[-2]['text'] = 'Old password wrong!'
        elif self.password_new_var.get() != self.password_sec_var.get():
            self.Label_fillup[-2]['text'] = 'Second password is different from the first!'

class editInfoMain(Frame):
    def __init__(self, username, b1, b2, master = None):
        Frame.__init__(self, master, bg = 'AntiqueWhite')
        self.username = username
        self.root = master

        self.b1 = b1
        self.b2 = b2
        self.usernameVar = StringVar()

        self.imageAddress = userInformation.getPhotoInfo(self.username)

        self.createFrame()

    def createFrame(self):
        self.Frame_main = Frame(self.root, bg = "AntiqueWhite")
        self.Frame_main.pack()

        Label_fillup = []
        for i in range(0,1):
            Label_fillup.append(Label(self.Frame_main, bg = "AntiqueWhite"))
            Label_fillup[i].pack(anchor = NW)

        Frame_photo = Frame(self.Frame_main, bg = "AntiqueWhite")
        Frame_photo.pack(anchor = NW, ipadx = 50)
        Frame_username = Frame(self.Frame_main, bg = "AntiqueWhite")
        Frame_username.pack(anchor = NW, ipadx = 70)
        Frame_password = Frame(self.Frame_main, bg = "AntiqueWhite")
        Frame_password.pack(anchor = NW, ipadx = 100)
        Frame_user_info = Frame(self.Frame_main, bg = "AntiqueWhite")
        Frame_user_info.pack(anchor = NW, ipadx = 100)
        Frame_restaurant_pref = Frame(self.Frame_main, bg = "AntiqueWhite")
        Frame_restaurant_pref.pack(anchor = NW, ipadx = 100)
        Frame_accept_cancel = Frame(self.Frame_main, bg = "AntiqueWhite")
        Frame_accept_cancel.pack(anchor = NW, ipadx = 100)

        font_label = font.Font(size = 15)
        font_button = font.Font(size = 12, family = "Arial", weight = font.BOLD)
        font_button_normal = font.Font(size = 10, family = "Arial")
        font_entry = font.Font(size = 10, family = "Arial")

        Label_profile_photo = Label(Frame_photo, text = "Profile Photo", bg = "AntiqueWhite", font = font_label)
        Label_profile_photo.pack(anchor = N, side = LEFT, ipady = 40)

        load_profile_photo = Image.open(self.imageAddress)
        load_profile_photo = self.resize(100,100,load_profile_photo)
        render_profile_photo = ImageTk.PhotoImage(load_profile_photo)

        Button_photo = Button(Frame_photo, image = render_profile_photo, bd = 0)
        Button_photo.image = render_profile_photo
        Button_photo.pack(anchor = N, side = RIGHT)

        Label_fillup.append(Label(Frame_username, bg = "AntiqueWhite"))
        Label_fillup[-1].pack()
        Label_username = Label(Frame_username, text = "Username", bg = "AntiqueWhite", font = font_label)
        Label_username.pack(anchor = N, side = LEFT)
        Entry_username = Entry(Frame_username, textvariable = self.usernameVar, width = 15, bg = "AliceBlue", font = font_entry)
        Entry_username.pack(anchor = N, side = RIGHT, ipady = 5)
        self.usernameVar.set(self.username)

        Label_fillup.append(Label(Frame_password, bg = "AntiqueWhite"))
        Label_fillup[-1].pack()
        Label_password = Label(Frame_password, text= "Password", bg = "AntiqueWhite", font = font_label)
        Label_password.pack(anchor = N, side = LEFT)
        Button_password = Button(Frame_password, text = "Edit", bg = "WhiteSmoke", font = font_button_normal, bd = 3, command = self.editPassword)
        Button_password.pack(anchor = N, side = RIGHT, ipadx = 5)

        Label_fillup.append(Label(Frame_user_info, bg = "AntiqueWhite"))
        Label_fillup[-1].pack()
        Label_user_info = Label(Frame_user_info, text = "User Information", bg = "AntiqueWhite", font = font_label)
        Label_user_info.pack(anchor = N, side = LEFT)
        Button_user_info = Button(Frame_user_info, text = "Edit", bg = "WhiteSmoke", font = font_button_normal, bd = 3, command = self.editPersonalInfoCallback)
        Button_user_info.pack(anchor = N, side = RIGHT, ipadx = 5)

        Label_fillup.append(Label(Frame_restaurant_pref, bg = "AntiqueWhite"))
        Label_fillup[-1].pack()
        Label_restaurant_pref = Label(Frame_restaurant_pref, text= "Restaurant Preference", bg = "AntiqueWhite", font = font_label)
        Label_restaurant_pref.pack(anchor = N, side = LEFT)
        Button_restaurant_pref = Button(Frame_restaurant_pref, text = "Edit", bg = "WhiteSmoke", font = font_button_normal, bd = 3, command = self.editPreferenceCallbac)
        Button_restaurant_pref.pack(anchor = N, side = RIGHT, ipadx = 5)
        Label_fillup.append(Label(Frame_restaurant_pref, bg = "AntiqueWhite"))
        Label_fillup[-1].pack()

        for i in range(0,2):
            Label_fillup.append(Label(Frame_accept_cancel, bg = "AntiqueWhite", width = 4))
            Label_fillup[-1].grid(row = 0, column = i)
        Button_accept = Button(Frame_accept_cancel, text = "Accept", bg = "Green", bd = 4, font = font_button, command = self.acceptCallback)
        Button_accept.grid(row = 0, column = 3, ipady = 5, ipadx = 5)
        Button_cancel = Button(Frame_accept_cancel, text = "Cancel", bg = "Red", bd = 4, font = font_button, command = self.cancelCallback)
        Button_cancel.grid(row = 0, column = 4, ipady = 5, ipadx = 5)

    def editPersonalInfoCallback(self):
        self.Frame_main.destroy()
        personal_info = editUserInfo(self.username, self.root)
        personal_info.pack()

    def editPreferenceCallbac(self):
        self.Frame_main.destroy()
        preference_info = editPreference(self.username, self.root)
        preference_info.pack()

    def editPassword(self):
        self.Frame_main.destroy()
        password_info = editPassword(self.username, self.root)
        password_info.pack()

    def acceptCallback(self):
        if not self.username == self.usernameVar.get() and self.usernameVar.get() != "":
            userInformation.updateUserName(self.username, self.usernameVar.get())
            file = open('./Info/temp.txt', 'r+')
            file.write(self.usernameVar.get())
            file.close()
            messagebox.showinfo("Update success!", "Your username had been successfully updated!")
        else:
            messagebox.showinfo("Sorry...", "Something is wrong, please try again later")

    def cancelCallback(self):
        self.root.withdraw()
        self.destroy()
        with open('./Info/temp.txt', 'r+') as file:
            file.truncate()

        userInformation.updateUserName(self.usernameVar.get(), self.username)

        self.b1['state'] = 'normal'
        self.b2['state'] = 'normal'

    def resize(self, w_box, h_box, image):
        w, h = image.size
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h

        factor = min([f1,f2])

        width = int(w*factor)
        height = int(h*factor)

        return image.resize((width,height), Image.ANTIALIAS)