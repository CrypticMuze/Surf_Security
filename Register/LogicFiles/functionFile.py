from itertools import permutations
import hashlib

def convertToString(list):
    string = ""
    for element in list:
        string += element
    return string

def createDefaultIteration(chunkList):
    defaultIteration = []
    for number in chunkList:
        if (number >= 0 and number <= 5):
            defaultIteration.append('a')
        elif (number >= 6 and number <= 11):
            defaultIteration.append('b')
        elif (number >= 12 and number <= 17):
            defaultIteration.append('c')
        elif (number >= 18 and number <= 23):
            defaultIteration.append('d')
        elif (number >= 24 and number <= 29):
            defaultIteration.append('e')
        elif (number >= 30 and number <= 35):
            defaultIteration.append('f')
        elif (number >= 36 and number <= 41):
            defaultIteration.append('g')
        elif (number >= 42 and number <= 47):
            defaultIteration.append('h')
        elif (number >= 48 and number <= 53):
            defaultIteration.append('i')
        elif (number >= 54 and number <= 59):
            defaultIteration.append('j')
        elif (number >= 60 and number <= 65):
            defaultIteration.append('k')
        elif (number >= 66 and number <= 71):
            defaultIteration.append('l')
        elif (number >= 72 and number <= 77):
            defaultIteration.append('m')
        elif (number >= 78 and number <= 83):
            defaultIteration.append('n')
        elif (number >= 84 and number <= 91):
            defaultIteration.append('#')
        elif (number >= 92 and number <= 99):
            defaultIteration.append('*')
        else:
            print("Not a valid chunk")
    return defaultIteration

def convertEachPermutationListToString(everyPermutation):
    everyPermutationList = []
    for permutation in everyPermutation:
        permutation = convertToString(permutation)
        everyPermutationList.append(permutation)
    return everyPermutationList

def hashEveryPermutation(everyPermutationList):
    everyHashedPermutationList = []
    for permutation in everyPermutationList:
        result = hashlib.md5(permutation.encode())
        everyHashedPermutationList.append(result.hexdigest())
    return everyHashedPermutationList

def hashLoginPassword(passwordLogin):
    passwordLogin = hashlib.md5(passwordLogin.encode())
    passwordLogin = passwordLogin.hexdigest()
    return passwordLogin

def makePasswordEven(dummyPassword):
    integerList = [int(x) for x in dummyPassword]
    print(integerList)
    print(type(integerList))
    integerList.append(9)
    print(integerList)