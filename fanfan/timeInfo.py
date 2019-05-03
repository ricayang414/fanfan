import time

def calculateDate(year, month, day, remainingday):
    while remainingday>0:
        day += 1
        remainingday -= 1
        if month in [1,3,5,7,8,10]:
            if day == 32:
                return calculateDate(year, month + 1, 1, remainingday)
        elif month in [4,6,9,11]:
            if day == 31:
                return calculateDate(year, month + 1, 1, remainingday)
        elif month == 2 and year%4 == 0:
            if day == 30:
                return calculateDate(year, month + 1, 1, remainingday)
        elif month == 2 and year%4 != 0:
            if day == 29:
                return calculateDate(year, month + 1, 1, remainingday)
        elif month == 12:
            if day == 32:
                return calculateDate(year + 1, 1, 1, remainingday)
        else:
            return calculateDate(year, month, day, remainingday)
    return [year,month,day]

def generateDateRangeToEndOfMonth(year,month, day):
    if month in [1,3,5,7,8,10,12]:
        return tuple(range(day,32))
    if month in [4,6,9,11]:
        return tuple(range(day,31))
    if month == 2 and year % 4 == 0:
        return tuple(range(day,30))
    else:
        return tuple(range(day,29))

def generateMonthRangeAcrossYear(startMonth, endMonth):
    result = list(range(startMonth, 13))
    result += list(range(1, endMonth + 1))
    return result

def readTimeSpan():
    original = open('./Info/timeInfo.txt', 'r')
    file = original.read()
    original.close()
    result = []
    if not file == "":
        file = file.split("\n")
        for i in range(0, len(file)):
            result.append(file[i].split(";"))

        for i in range(0, len(result)):
            for j in range(1, len(result[i])):
                result[i][j] = result[i][j].split(",")


    return result

def checkTimeSpan():
    file = readTimeSpan()
    currentTime = time.strftime("%Y%m%d", time.localtime())

    toDelete = []
    for i in file:
        toDelete = []
        for j in i:
            try:
                date = int(j[0])
            except:
                print()
            else:
                if date < int(currentTime):
                    toDelete.append(j)

        for j in toDelete:
            i.remove(j)

    newFile = open('./Info/timeInfo.txt', 'r+')
    newFile.truncate()

    for i in range(0, len(file)):
        if i == 0:
            toWrite = file[i][0] + ";"
        else:
            toWrite = "\n" + file[i][0] + ";"

        for j in file[i]:
            if type(j) == list:
                for m in j:
                    toWrite += m + ","
                toWrite = toWrite[:-1] + ";"

        toWrite = toWrite[:-1]
        newFile.write(toWrite)

def writeTimeInfo(timeInformation):
    file = readTimeSpan()

    writeFile = open('./Info/timeInfo.txt', 'a+')
    inList = False
    isExist = False

    toWrite = ""
    finalResult = ""

    if len(file) == 0:
        toWrite = timeInformation[0] + ";"
        for i in timeInformation:
            if type(i) == list:
                toWrite += toSingleString(i)
        toWrite = toWrite[:-1]
        writeFile.write(toWrite)
    else:
        for i in range(0, len(file)):
            if file[i][0]  == timeInformation[0]:
                if not isTimeSpanExist(timeInformation[0], timeInformation[1]):
                    file[i].append(timeInformation[1])
                inList = True
        if inList:
            for i in range(0, len(file)):
                if i == 0:
                    toWrite = file[i][0] + ";"
                else:
                    toWrite = "\n" + file[i][0] + ";"
                for j in file[i]:
                    if type(j) == list:
                        toWrite += toSingleString(j)
                toWrite = toWrite[:-1]
                finalResult += toWrite
            writeFile = open('./Info/timeInfo.txt', 'r+')
            writeFile.write(finalResult)
        else:
            toWrite = "\n" + timeInformation[0] + ";"
            for i in timeInformation:
                if type(i) == list:
                    toWrite += toSingleString(i)
            toWrite = toWrite[:-1]
            writeFile.write(toWrite)
    writeFile.close()

def toSingleString(L):
    result = ""
    for i in L:
        result += i + ","
    result = result[:-1] + ";"

    return result

def isTimeSpanExist(username, timeSpan):
    times = readTimeSpan()
    result = False

    for i in times:
        if i[0] == username:
            for j in i:
                if type(j) == list:
                    if timeSpan[0] == j[0] and timeSpan[1] == j[1] and timeSpan[2] == j[2]:
                        result = True

    return result

def checkIfTimeMatch(username1, username2):
    file = readTimeSpan()
    person1 = []
    person2 = []
    for i in file:
        if i[0] == username1:
            person1 = i
        if i[0] == username2:
            person2 = i
    if len(person1) == 0 or len(person1) == 1 or len(person2) == 0 or len(person2) == 1:
        return False

    for i in person1:
        for j in person2:
            if type(i) == list and type(j) == list:
                isDifferent = False
                for k in range(0,3):
                    if i[k] != j[k]:
                        isDifferent = True
                if not isDifferent:
                    return i

    return False

checkTimeSpan()