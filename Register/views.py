from django.shortcuts import render
from .forms import SignUpForm
from .LogicFiles.addUser import register

def RegisterUser(request):

	context = {}

	data = SignUpForm(request.POST or None)
	if(data.is_valid()):
		userdata = data.cleaned_data
		register(userdata)

	context['form'] = SignUpForm()

	return render(request, "Register/Register.html", context)

