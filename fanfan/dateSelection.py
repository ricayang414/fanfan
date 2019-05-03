from tkinter import messagebox
from tkinter import *
import time
from tkinter import ttk
from PIL import Image, ImageTk
import calendar

class timeSelection(object):
    def __init__(self, master = None):
        self.root = master

        self.months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

        self.year_var = StringVar()
        self.month_var = StringVar()
        self.day_var = []

        self.current_date = time.strftime("%Y%m%d", time.localtime())
        self.current_year = time.strftime("%Y", time.localtime())
        self.current_month = time.strftime("%B", time.localtime())
        self.createFrame()


    def createFrame(self):
        Label_fillup = Label(self.root, bg = "AntiqueWhite")
        Label_fillup.pack()

        comboBox_year = ttk.Combobox(self.root, width = 20, textvariable = self.year_var, state = "readonly")
        comboBox_year['value'] = tuple(range(1970, int(self.current_year) + 1))
        self.year_var.set(str(self.current_year))
        comboBox_year.pack()

        comboBox_year.bind("<<ComboboxSelected>>", self.selected)

        image_left = Image.open('./left.jpg')
        image_left = self.resize(20, 20, image_left)
        render_left = ImageTk.PhotoImage(image_left)

        Frame_month = Frame(self.root)
        Frame_month.pack()
        Button_left = Button(Frame_month, image = render_left, bd = 1, command = self.leftCallBack)
        Button_left.image = render_left
        Button_left.grid(row = 0, column = 0)

        comboBox_month = ttk.Combobox(Frame_month, textvariable = self.month_var, width = 12, state = "readonly")
        comboBox_month['value'] = self.months
        self.month_var.set(self.current_month)
        comboBox_month.grid(row = 0, column = 1, ipady = 1)

        comboBox_month.bind("<<ComboboxSelected>>", self.selected)

        image_right = Image.open('./right.jpg')
        image_right = self.resize(20, 20, image_right)
        render_right = ImageTk.PhotoImage(image_right)
        Button_right = Button(Frame_month, image = render_right, bd = 1, command = self.rightCallBack)
        Button_right.image = render_right
        Button_right.grid(row = 0, column = 2)

        Frame_day = Frame(self.root)
        Frame_day.pack()
        week_day = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
        self.week_day = []
        for i in range(0, 7):
            color = "SkyBlue" if i % 2 == 0 else "AntiqueWhite"
            self.week_day.append(Label(Frame_day, text = week_day[i], bg = color, width = 2))
            self.week_day[i].grid(row = 0, column = i)

        self.Buttons_days = []
        for i in range(0, 42):
            color = "SkyBlue" if (i + 1) % 2 == 0 else "AntiqueWhite"
            self.day_var.append(StringVar())
            self.Buttons_days.append(Button(Frame_day, text = "", bg = color, width = 2, bd = 0, command = lambda i = i:self.dayCallBack(i)))
            self.Buttons_days[i].grid(row = i // 7 + 1, column = i % 7)

        days_length = self.calculateDays(int(self.year_var.get()), self.month_var.get())
        start_day = self.calculateStartDay(self.year_var.get(), self.month_var.get())

        for i in range(start_day, start_day + days_length):
            self.day_var[i].set(str(i - start_day + 1))
            self.Buttons_days[i]['text'] = str(i - start_day + 1)

        for i in range(0,42):
            if self.day_var[i].get() == "":
                self.Buttons_days[i]['state'] = "disable"
                self.Buttons_days[i]['bg'] = "AntiqueWhite"

    def leftCallBack(self):
        if not (self.year_var.get() == "1970" and self.month_var.get() == "January"):
            if self.month_var.get() == "January":
                self.year_var.set(int(self.year_var.get()) - 1)
                self.month_var.set("December")
            else:
                for i in range(0, 12):
                    if self.months[i] == self.month_var.get():
                        self.month_var.set(self.months[i - 1])
                        break
            self.selected("")

    def rightCallBack(self):
        if not (self.year_var.get() == self.current_year and self.month_var.get() == "December"):
            if self.month_var.get() == "December":
                self.year_var.set(int(self.year_var.get()) + 1)
                self.month_var.set("January")
            else:
                for i in range(0, 12):
                    if self.months[i] == self.month_var.get():
                        self.month_var.set(self.months[i + 1])
                        break

            self.selected("")

    def selected(self,a):
        days_length = self.calculateDays(int(self.year_var.get()), self.month_var.get())
        start_day = self.calculateStartDay(self.year_var.get(), self.month_var.get())

        self.reset()

        for i in range(start_day, start_day + days_length):
            self.day_var[i].set(str(i - start_day + 1))
            self.Buttons_days[i]['text'] = str(i - start_day + 1)

        for i in range(0,42):
            if self.day_var[i].get() == "":
                self.Buttons_days[i]['state'] = "disable"
                self.Buttons_days[i]['bg'] = "AntiqueWhite"

    def calculateDays(self, year, month):
        if year % 4  == 0:
            if month == "February":
                return 29
        else:
            if month == "February":
                return 28

        if month in ["January", "March", "May", "July", "August", "October", "December"]:
            return 31
        else:
            return 30

    def calculateStartDay(self, year, month):
        time_ori = time.strptime(str(year) + str(month) + "01", "%Y%B%d")
        time_week_day = time.strftime("%w", time_ori)
        return int(time_week_day)

    def dayCallBack(self, index):

        start_day = self.calculateStartDay(self.year_var.get(), self.month_var.get())
        day = str(int(index) - start_day + 1)
        day = "0" + day if len(day) == 1 else day

        month = str(list(calendar.month_name).index(self.month_var.get()))
        month = "0" + month if len(month) == 1 else month

        if int(str(self.year_var.get()) + month + day) >= int(self.current_date):
            messagebox.showinfo("Sorry!", "Please select correct date of birth!")

        else:
            age = self.calculateAge(self.year_var.get(), list(calendar.month_name).index(self.month_var.get()), day)
            callback = messagebox.askyesno("Confirm", "Are you sure this is your birthday?"
                                                      "\n" + self.month_var.get() + "/" + day + "/" + str(self.year_var.get()))
            if callback:
                with open('./Info/temp.txt', 'r+') as temp_file:
                    temp_file.truncate()
                    date_of_birth = str(self.year_var.get()) + month + day
                    temp_file.write(date_of_birth + ";" + str(age))
                    self.root.destroy()

    def resize(self, w_box, h_box, image):
        w, h = image.size
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h

        factor = min([f1,f2])

        width = int(w*factor)
        height = int(h*factor)

        return image.resize((width,height), Image.ANTIALIAS)

    def reset(self):
        for i in range(0, 42):
            self.day_var[i].set("")
            self.Buttons_days[i]['text'] = ""
            self.Buttons_days[i]['state'] = 'normal'
            color = "SkyBlue" if i % 2 == 0 else "AntiqueWhite"
            self.Buttons_days[i]['bg'] = color

    def calculateAge(self, year, month, day):
        if int(str(month) + str(day)) <= int(time.strftime("%m%d", time.localtime())):
            return int(self.current_year) - int(year)
        else:
            return int(self.current_year) - int(year) - 1