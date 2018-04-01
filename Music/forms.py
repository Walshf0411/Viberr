# The user model is being imported to tweak it
# as we dont want it be as default that is provided by django
from django.contrib.auth.models import User
from django import forms

# Inherited the base form class
class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

