from django.shortcuts import render, redirect
import random
from .LogicFiles.loginUser import signin
current = ''
username = ''


def dashboard(request):
    context = {}
    context['username'] = username

    if request.GET.get("logout"):
        return redirect("/login/")

    return render(request, "Login/dashboard.html", context)


def LoginUser(request):
    context = {}
    displayValue = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '#', '*']
    random.shuffle(displayValue)

    choiceList = [0, 1]
    choice = random.choice(choiceList)


    context['displayvaluebuttonone'] = displayValue[0]
    context['displayvaluebuttontwo'] = displayValue[1]
    context['displayvaluebuttonthree'] = displayValue[2]
    context['displayvaluebuttonfour'] = displayValue[3]
    context['displayvaluebuttonfive'] = displayValue[4]
    context['displayvaluebuttonsix'] = displayValue[5]
    context['displayvaluebuttonseven'] = displayValue[6]
    context['displayvaluebuttoneight'] = displayValue[7]
    context['displayvaluebuttonnine'] = displayValue[8]
    context['displayvaluebuttonten'] = displayValue[9]
    context['displayvaluebuttoneleven'] = displayValue[10]
    context['displayvaluebuttontwelve'] = displayValue[11]
    context['displayvaluebuttonthirteen'] = displayValue[12]
    context['displayvaluebuttonfourteen'] = displayValue[13]
    context['displayvaluebuttonfifteen'] = displayValue[14]
    context['displayvaluebuttonsixteen'] = displayValue[15]

    if (choice == 0):
        context['pattern'] = 'Pattern Horizontal'
        context['buttononevalue'] = 'a'
        context['buttontwovalue'] = 'b'
        context['buttonthreevalue'] = 'c'
        context['buttonfourvalue'] = 'd'
        context['buttonfivevalue'] = 'e'
        context['buttonsixvalue'] = 'f'
        context['buttonsevenvalue'] = 'g'
        context['buttoneightvalue'] = 'h'
        context['buttonninevalue'] = 'i'
        context['buttontenvalue'] = 'j'
        context['buttonelevenvalue'] = 'k'
        context['buttontwelvevalue'] = 'l'
        context['buttonthirteenvalue'] = 'm'
        context['buttonfourteenvalue'] = 'n'
        context['buttonfifteenvalue'] = '#'
        context['buttonsixteenvalue'] = '*'

    elif(choice ==1):
        context['pattern'] = 'Pattern Vertical'
        context['buttononevalue'] = 'a'
        context['buttontwovalue'] = 'e'
        context['buttonthreevalue'] = 'i'
        context['buttonfourvalue'] = 'm'
        context['buttonfivevalue'] = 'b'
        context['buttonsixvalue'] = 'f'
        context['buttonsevenvalue'] = 'j'
        context['buttoneightvalue'] = 'n'
        context['buttonninevalue'] = 'c'
        context['buttontenvalue'] = 'g'
        context['buttonelevenvalue'] = 'k'
        context['buttontwelvevalue'] = '#'
        context['buttonthirteenvalue'] = 'd'
        context['buttonfourteenvalue'] = 'h'
        context['buttonfifteenvalue'] = 'l'
        context['buttonsixteenvalue'] = '*'

    logindata = request.POST or None
    if request.POST.get("pass"):
        global current
        current = current + logindata['pass']

    if request.POST.get("save"):
        print(logindata['username'])
        print(logindata['password'])
        global username
        username = logindata['username']
        signin(logindata['username'], logindata['password'])
        return redirect("/login/dashboard")

    return render(request, "Login/Login.html", context)

def firstLayerAuthentication(request):

    firstLayerData = request.POST or None
    
    if request.POST.get("firstLayerSave"):
        answer = firstLayerData['answer']
        print(answer)
        if(answer == "Yes"):
            return redirect('/login/actualLogin')

    return render(request, "Login/firstLayer.html")

def phoneLayer(request):
    phoneLayerData = request.POST or None
    if request.POST.get("phoneLayerSave"):
        phoneNo = phoneLayerData["phone"]
        print(phoneNo)
        return redirect('/login/firstLogin')
    return render(request, "Login/phoneLayer.html")