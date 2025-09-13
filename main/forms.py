from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'reason', 'how_found', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'p-2 border border-black rounded-md w-full mb-4 placeholder-black font-bold',
                'placeholder': 'Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'p-2 border border-black rounded-md w-full mb-4 placeholder-black font-bold',
                'placeholder': 'Email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'p-2 border border-black rounded-md w-full mb-4 placeholder-black font-bold',
                'placeholder': 'Phone number',
            }),
            'reason': forms.Select(attrs={
                'class': 'p-2 border border-black rounded-md w-full mb-4 text-black font-bold',
                'placeholder': 'Reason to Contact',
            }),
            'how_found': forms.Select(attrs={
                'class': 'p-2 border border-black rounded-md w-full mb-4 text-black font-bold',
                'placeholder': 'How did you find about us?',
            }),
            'message': forms.Textarea(attrs={
                'class': 'p-2 border border-black rounded-md w-full mb-4 placeholder-black font-bold',
                'rows': 5,
                'placeholder': 'Message',
            }),
        }

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']