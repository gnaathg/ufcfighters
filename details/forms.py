from django import forms
from .models import Fighters
from django.contrib.auth.models import User

class FightersForm(forms.ModelForm):
    class Meta:
        model = Fighters
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "gender": forms.Select(attrs={"class": "form-control form-select"}),
            "blood": forms.Select(attrs={"class": "form-control form-select"}),
            "fighting_style": forms.Select(attrs={"class": "form-control form-select"}),
            "weight_class": forms.Select(attrs={"class": "form-control form-select"}),
            "picture": forms.FileInput(attrs={"class": "form-control"}),
        }
class SignupForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ["username","password","email"]

class SigninForm(forms.Form):

    username = forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput())