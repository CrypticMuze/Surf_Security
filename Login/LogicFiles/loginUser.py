from .connectToDatabase import *
from .functionFile import *

def signin(usernameLogin, passwordLogin):

    searchSQLQuery = "SELECT * from  users WHERE username = %s"
    usernameLogin = (usernameLogin,)
    cursor.execute(searchSQLQuery, usernameLogin)

    result = cursor.fetchall()

    passwordLogin = hashLoginPassword(passwordLogin)

    count = 0
    for row in result:
        for element in row:
            if (element == passwordLogin):
                count = 1
                break
    if(count == 1):
        print("Login Success")
    else:
        print("Login Fail")
