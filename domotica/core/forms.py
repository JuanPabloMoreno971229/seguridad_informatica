from cProfile import label
from tkinter import Widget
from django import forms
from .models import data_login


class LoginForm(forms.ModelForm):

    mail = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder':'Email/ User Name', 'id': 'inputFields1', 'type': 'text'}
    ))
    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder':'Password', 'id': 'inputFields2', 'type': 'password'}
    ))

    class Meta:
        model = data_login
        fields = '__all__'
        
        
    
    
