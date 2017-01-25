from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Please enter your name', max_length=100)