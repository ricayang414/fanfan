def findSemiColon(str, num):
    count = 0
    index = 0
    for i in str:
        if i == ";":
            count += 1
        if count == num:
            return index
        index += 1

def listToStringWithComma(L):
    result = ""
    for i in L:
        result += i + ","

    result = result[:-1]
    return result
