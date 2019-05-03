import time

def readAppointment():
    file = open('./Info/appointmentInfo.txt', 'r')

    temp = file.read()
    if temp != "":
        if temp.find("\n") != -1:
            temp = temp.split("\n")
            for i in range(0, len(temp)):
                temp[i] = temp[i].split(";")
                temp[i][2] = temp[i][2].split(",")
        else:
            temp = temp.split(";")
            temp[2] = temp[2].split(",")

    return temp

def writeAppointment(appointment):
    file = open('./Info/appointmentInfo.txt', 'r+')
    toWrite = ""

    if isExist(appointment[0], appointment[2][0]) or isExist(appointment[1], appointment[2][0]):
        return False

    if file.read() == "":
        toWrite = listToString(appointment)
    else:
        toWrite = "\n" + listToString(appointment)

    file.write(toWrite)
    file.close()
    return True

def listToString(L):
    result = ""
    for i in L:
        if type(i) == list:
            for j in i:
                result += j + ","
            result = result[:-1] + ";"
        else:
            result += i + ";"
    result = result[:-1]
    return result

def stringToList(S):
    temp = S.split(";")
    for i in range(0,len(temp)):
        if temp[i].find(",") != -1:
            temp[i] = temp[i].split(",")

    return temp

# appointmentTime should be a list, which contains[date,lunch/dinner,time span]
# this method is to be asserted before selecting restaurant to validate if the time is validated
# return true if an appointment already exist
# return false if any appointment does not exist
def isExist(username, date):
    appointments = readAppointment()
    for i in appointments:
        if i[0] == username or i[1] == username:
            if i[2][0] == date:
                return True

    return False

# return format: list of appointments
# every appointment should be like
# [nameOfTheOtherPerson, dateAndTime, whichRestaurant]
def getAppointment(username):
    appointments = readAppointment()
    result = []
    for i in appointments:
        if i[0] == username:
            result.append([i[1], i[2], i[3]])
        elif i[1] == username:
            result.append([i[0], i[2], i[3]])

    return result

def listToDateInfo(L):
    month = L[0][4:6]
    if month[0] == "0":
        month = month[1]
    day = L[0][6:]
    if day[0] == "0":
        day = day[1]

    date = L[0][:4] + month + day

    date = time.strptime(date, '%Y%m%d')
    date = time.strftime('%b/%d/%Y', date)

    if L[1] == "lunch":
        ampm = "pm" if L[2] == "11:30-12:00" or L[2] == "12:00-12:30" or L[2] == "12:30-1:00" or L[2] == "1:00-1:30" or L[2] == "1:30-2:00" else "am"
    else:
        ampm = "pm"

    date += " " + L[2] + ampm

    return date
