import restaurant
import random
import userInformation
import timeInfo
import appointmentInfo

def selectRestaurant(userPreference, users):
    matchedPerson = []
    matchedTimeSpan = []

    for i in users:
        if i[0] != userPreference[0]:
            if restaurant.matchAgeAndGender(i, userPreference[1], userPreference[2]):
                if restaurant.matchTopicsAndJob(i, userPreference[5], userPreference[6]):
                    timeMatch = timeInfo.checkIfTimeMatch(userPreference[0], i[0])
                    if timeMatch:
                        matchedPerson.append(i[0])
                        matchedTimeSpan.append([i[0],timeMatch])

    if len(matchedPerson) == 0:
        return []

    possiblePersons = []

    for i in matchedPerson:
        selected = restaurant.matchRestaurant(userInformation.searchUserInfo(i), userPreference[3], userPreference[4])
        if not len(selected) == 0:
            possiblePersons.append([i, selected])

    if len(possiblePersons) == 0:
        return []

    randNum = 0
    randNum2 = 0

    print(possiblePersons)

    if len(possiblePersons) == 1:
        timeSpan = []
        for i in matchedTimeSpan:
            if i[0] == possiblePersons[0][0]:
                timeSpan = i
        if len(possiblePersons[0][1]) == 1:
            result = appointmentInfo.writeAppointment([userPreference[0],timeSpan[0],timeSpan[1],possiblePersons[0][1][0][0]])
            if not result:
                return [possiblePersons[0][0], possiblePersons[0][1][0]]
            else:
                return []
        else:
            randNum2 = random.randint(0,len(possiblePersons[0][1])) - 1
            result = appointmentInfo.writeAppointment([userPreference[0],timeSpan[0],timeSpan[1],possiblePersons[0][1][randNum2]])
            if not result:
                return [possiblePersons[0][0], possiblePersons[0][1][randNum2]]
            else:
                return []
    else:
        randNum = random.randint(1,len(possiblePersons)) - 1
        timeSpan = []
        for i in matchedTimeSpan:
            if i[0] == possiblePersons[0][0]:
                timeSpan = i
        if len(possiblePersons[randNum][1]) == 1:
            result = appointmentInfo.writeAppointment([userPreference[0],timeSpan[0],timeSpan[1],possiblePersons[randNum][1][0]])
            if not result:
                return [[possiblePersons[randNum][0]], possiblePersons[randNum][1][0]]
            else:
                return []
        else:
            randNum2 = random.randint(1,len(possiblePersons[randNum][1])) - 1
            result = appointmentInfo.writeAppointment([userPreference[0],timeSpan[0],timeSpan[1],possiblePersons[randNum][randNum2][0]])
            if not result:
                return [possiblePersons[randNum][randNum2], possiblePersons[randNum][1][randNum2]]
            else:
                return []
