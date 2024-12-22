from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
            'class': 'w-full px-4 py-2 rounded-lg text-base font-normal border border-gray-600 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500',
            'style': 'background-color: rgba(255, 255, 255, 0.6); color: black;',
            'placeholder': 'Write your tweet...',
            'rows': 4,
            }),

            'photo': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 text-base font-normal py-2 bg-gray-700 bg-opacity-40 text-white rounded-lg border border-gray-600 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500',
                'style': 'background-color: rgba(255, 255, 255, 0.6); color: black;',
            }),
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

