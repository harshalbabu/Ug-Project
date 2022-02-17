from django import forms

class PassangerForm(forms.Form):
    name = forms.CharField()