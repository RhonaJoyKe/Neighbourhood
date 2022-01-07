from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Post,Business,NeighbourHood
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','image')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'email','description')
class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        exclude = ('admin',)



