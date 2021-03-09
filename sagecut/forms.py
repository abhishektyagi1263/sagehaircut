from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo, customer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta():
        model = User
        fields = ('username','email','password')
        widgets = {
            'username': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'email': forms.TextInput(
    				attrs={
    					'class': 'form-control'
    					}
    				),
            }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields =('phonenum',)
        widgets = {
            'phonenum': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            }


class NewUser(forms.ModelForm):

    class Meta():
        model = customer
        fields = ('first_name','email','set_date','set_time')
    
