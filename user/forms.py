from django import forms
from user.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreatUserForm(UserCreationForm):
    email=forms.EmailField(required=True)
    
    class Meta:
        model= User
        fields=['username','email','password1','password2']
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['phone','image']