from .connectToDatabase import *
from .functionFile import *

integerList = []
chunkList = []
defaultIteration = []
everyPermutationList = []
everyHashedPermutationList = []

def check(username):
    checkSqlQuery = "SELECT * FROM users WHERE username = %s"
    value = (username,)
    cursor.execute(checkSqlQuery, value)
    result = cursor.fetchall()
    if(len(result)>0):
        return True
    else:
        return False

def register(userdata):

    dummyUserName = userdata['username']
    dummyPassword = userdata['password']
    dummyEmail = userdata['email']

    isPresent = check(dummyUserName)

    if(isPresent):
        print("Username Already Exist")
    else:
        if (len(dummyPassword) % 2 == 0):

            integerList = [int(x) for x in dummyPassword]

            for i in range(0, int(len(integerList)), 2):
                chunk = (integerList[i] * 10) + integerList[i + 1]
                chunkList.append(chunk)

            defaultIteration = createDefaultIteration(chunkList)
            print(defaultIteration)

            defaultString = convertToString(defaultIteration)
            print(defaultString)

            everyPermutation = permutations(defaultString)

            everyPermutationList = convertEachPermutationListToString(everyPermutation)
            print(everyPermutationList)

            everyHashedPermutationList = hashEveryPermutation(everyPermutationList)
            print(everyHashedPermutationList)

            everyHashedPermutationList.insert(0, dummyPassword)
            everyHashedPermutationList.insert(0, dummyUserName)
            print(everyHashedPermutationList)

            insertSQLQuery = "INSERT INTO users (username, originalPass, pass1, pass2, pass3, pass4, pass5, pass6, pass7, " \
                             "pass8, pass9, pass10, pass11, pass12, pass13, pass14, pass15, pass16, pass17, pass18, pass19, " \
                             "pass20, pass21, pass22, pass23, pass24, email) VALUES("

            for element in everyHashedPermutationList:
                insertSQLQuery += "'"
                insertSQLQuery += element
                insertSQLQuery += "'"
                insertSQLQuery += ','

            insertSQLQuery += "'"
            insertSQLQuery += dummyEmail
            insertSQLQuery += "'"
            insertSQLQuery += ')'

            print(insertSQLQuery)
            cursor.execute(insertSQLQuery)

            mydb.commit()
            print("User Registered successfully")

        else:
            print("Password is odd LENGTH")
