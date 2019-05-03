import utility

def readUserInfo():
    file = open("./Info/userInfo.txt","r").read().split("\n")

    for i in range(0,len(file)):
        file[i] = file[i].split(";")

    for i in range(0,len(file)):
        file[i][4] = file[i][4].split(",")
        file[i][6] = file[i][6].split(",")
        file[i][7] = file[i][7].split(",")

    return file

def writeUserInfo(information):
    file = open("./Info/userInfo.txt", "r+")

    info = ""

    if(file.read() == ""):
        # info = information[0] + ";" + information[1]
        for i in range(0, len(information)):
            if not type(information[i]) == list:
                if not i == len(information) - 1:
                    info += information[i] + ";"
                else:
                    info += information[i]
            else:
                for j in range(0, len(information[i])):
                    if not j == len(information[i]) - 1:
                        info += information[i][j] + ","
                    else:
                        info += information[i][j] + ";"
    else:
        # info = "\r" + information[0] + ";" + information[1]
        for i in range(0, len(information)):
            if i == 0:
                info += "\n" + information[i] + ";"
            elif not type(information[i]) == list:
                if not i == len(information) - 1:
                    info += information[i] + ";"
                else:
                    info += information[i]

            else:
                for j in range(0, len(information[i])):
                    if not j == len(information[i]) - 1:
                        info += information[i][j] + ","
                    else:
                        info += information[i][j] + ";"

    file.write(info)

def writePhotoInfo(username, profilePhoto):
    file = open('./Info/profilePhotoInfo.txt', 'r+')

    if file.read() == "":
        file.write(username + ";" + profilePhoto)
    else:
        file.write("\r" + username + ";" + profilePhoto)

def getPhotoInfo(username):
    file = open('./Info/profilePhotoInfo.txt', 'r').read().split("\n")
    for i in range(0, len(file)):
        file[i] = file[i].split(";")

    for i in file:
        if username == i[0]:
            return i[1]

    return False

def returnUsername():
    users = readUserInfo()

    result = []
    for i in users:
        result.append(i[0])

    return result

def checkPassword(username, password):
    users = readUserInfo()
    result = False
    findUser = False
    for i in users:
        if username == i[0]:
            findUser = True
            if password == i[1]:
                result = True

    return result and findUser

def searchUserInfo(username):
    users = readUserInfo()

    for i in users:
        if i[0] == username:
            return i

    return False

def updateUserTaste(username, newTaste):
    users = readUserInfo()
    lineNum = 0
    for i in users:
        lineNum += 1
        if i[0] == username:
            break

    if lineNum == 0:
        return False

    newTaste = utility.listToStringWithComma(newTaste)
    users = open('./Info/userInfo.txt', 'r+')

    data = ""

    for i in users:
        lineNum -= 1
        if lineNum == 0:
            start = utility.findSemiColon(i,6) + 1
            end = utility.findSemiColon(i,7)
            toWrite = i[0:start] + newTaste + i[end:]
            data += toWrite
        else:
            data += i
    users.close()
    users = open('./Info/userInfo.txt', "r+")
    users.write(data)
    users.close()
    return True

def updatePriceRange(username, newPriceRange):
    users = readUserInfo()
    lineNum = 0
    for i in users:
        lineNum += 1
        if i[0] == username:
            break

    if lineNum == 0:
        return False

    newPriceRange = utility.listToStringWithComma(newPriceRange)
    users = open('./Info/userInfo.txt', 'r')

    data = ""

    for i in users:
        lineNum -= 1
        if lineNum == 0:
            start = utility.findSemiColon(i, 7) + 1
            end = utility.findSemiColon(i, 8)
            toWrite = i[0:start] + newPriceRange + i[end:]
            data += toWrite
        else:
            data += i

    users = open('./Info/userInfo.txt', 'r+')
    users.write(data)
    users.close()

    return True

def updateUserInfo(username, information):
    users = readUserInfo()
    user_index = 0

    for i in users:
        if i[0] == username:
            break
        user_index += 1

    toWrite = ""
    temp = ""

    file_write = open('./Info/userInfo.txt', 'r+')
    for i in file_write:
        if user_index == 0:
            # change the part of interested topics
            start = utility.findSemiColon(i, 4) + 1
            end = utility.findSemiColon(i, 5)
            temp_topics = utility.listToStringWithComma(information[0])

            temp = i[0:start] + temp_topics + i[end:]

            # change the part of job selection
            start = utility.findSemiColon(temp, 5) + 1
            end = utility.findSemiColon(temp, 6)

            temp = temp[0:start] + information[1] + temp[end:]
            print(temp)

            toWrite += temp

        else:
            toWrite += i

        user_index -= 1

    file_write = open('./Info/userInfo.txt', 'r+')
    file_write.write(toWrite)
    file_write.close()

def updateUserName(username_ori, username_new):
    toWrite = ""
    file = open('./Info/userInfo.txt', 'r+')
    for i in file:
        temp = i.split(";")
        if temp[0] == username_ori:
            end = utility.findSemiColon(i,1)
            toWrite += username_new + i[end:]
        else:
            toWrite += i

    file.close()
    file = open('./Info/userInfo.txt', 'r+')
    file.write(toWrite)

    # change username in timeInfo.txt
    toWrite = ""
    file = open('./info/timeInfo.txt', 'r')
    for i in file:
        temp = i.split(";")
        if temp[0] == username_ori:
            end = utility.findSemiColon(i,1)
            toWrite += username_new + i[end:]
        else:
            toWrite += i
    file.close()
    file = open('./Info/timeInfo.txt', 'r+')
    file.write(toWrite)

    # change username in profilePhotoInfo.txt
    toWrite = ""
    file = open('./Info/profilePhotoInfo.txt', 'r')
    for i in file:
        temp = i.split(";")
        if temp[0] == username_ori:
            end = utility.findSemiColon(i,1)
            toWrite += username_new + i[end:]
        else:
            toWrite += i
    file.close()
    file = open('./Info/profilePhotoInfo.txt', 'r+')
    file.write(toWrite)

    # change username in appointmentInfo.txt
    toWrite = ""
    file = open('./Info/appointmentInfo.txt', 'r')
    for i in file:
        temp = i.split(";")
        if temp[0] == username_ori:
            end = utility.findSemiColon(i,1)
            toWrite += username_new + i[end:]
        elif temp[1] == username_ori:
            start = utility.findSemiColon(i,1) + 1
            end = utility.findSemiColon(i,2)
            toWrite += i[:start] + username_new + i[end:]
        else:
            toWrite += i
    file.close()
    file = open('./Info/appointmentInfo.txt', 'r+')
    file.write(toWrite)