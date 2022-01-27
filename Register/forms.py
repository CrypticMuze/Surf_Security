from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Enter 8 digit number")
