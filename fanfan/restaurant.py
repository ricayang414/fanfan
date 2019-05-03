import random

def readRestaurant():
    file = open("./Info/restaurant.txt", "r").read().split("\n")

    for i in range(0,len(file)):
        file[i] = file[i].split(";")
        file[i][2] = file[i][2].split(",")

    return file

def transNameToNum(file):
    for i in range(0,len(file)):
        if file[i][1] == "Thailand":
            file[i][1] = 0
        elif file[i][1] == "Chinese":
            file[i][1] = 1
        elif file[i][1] == "Fast":
            file[i][1] = 2
        elif file[i][1] == "American":
            file[i][1] = 3
        elif file[i][1] == "Japanese":
            file[i][1] = 4
        elif file[i][1] == "Sea":
            file[i][1] = 5
        elif file[i][1] == "Italian":
            file[i][1] = 6
        elif file[i][1] == "Desert":
            file[i][1] = 7
        elif file[i][1] == "Korean":
            file[i][1] = 8
        elif file[i][1] == "Mexican":
            file[i][1] = 9
        elif file[i][1] == "Vietnam":
            file[i][1] = 10
        elif file[i][1] == "Peru":
            file[i][1] = 11
        elif file[i][1] == "African":
            file[i][1] = 12
        elif file[i][1] == "Vegetarian":
            file[i][1] = 13

    return file

def matchAgeAndGender(person, preferGender, preferAge):
    result = True

    if not person[2] <= preferAge[1] or not person[2] >= preferAge[0]:
        result = False
    if preferGender == 0 and person[3] == "female":
        result = False
    elif preferGender == 1 and person[3] == "male":
        result = False

    return result

def matchTopicsAndJob(person1, topics, job):
    result = True
    matchTime = 0
    for i in range(0, len(person1[4])):
        for j in range(0, len(topics)):
            if person1[4][i] == topics[j]:
                matchTime += 1

    if not person1[5] == job or matchTime < 2:
        result = False


    return result

def matchRestaurant(person1, taste, priceRange):
    matchPreference = []
    result = []
    for i in range(0, len(person1[6])):
        for j in range(0, len(taste)):
            if person1[6][i] == taste[j]:
                matchPreference.append(person1[6][i])

    if len(matchPreference) == 0:
        return []

    lowerPriceRange = person1[7][0] if person1[7][0] < priceRange[0] else priceRange[0]
    upperPriceRange = person1[7][0] if person1[7][0] > priceRange[0] else priceRange[0]

    if lowerPriceRange > upperPriceRange:
        return []

    matchedRestaurants = []

    for i in matchPreference:
        if not len(searchRestaurant(i)) == 0:
            temp = searchRestaurant(i)
            for j in temp:
                matchedRestaurants.append(j)

    for i in matchedRestaurants:
        if lowerPriceRange >= i[2][0] and lowerPriceRange <= i[2][1]:
            result.append(i)
        elif upperPriceRange <= i[2][1] and upperPriceRange >= i[2][0]:
            result.append(i)

    return result

def searchRestaurant(foodType):
    restaurants = readRestaurant()
    result = []
    for i in restaurants:
        if foodType == i[1]:
            result.append(i)

    return result