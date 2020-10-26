from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    ADMINISTRADOR = 'AD'
    LOGISTICO = 'LO'
    PRODUCTIVO = 'PR'
    CONTROLO = 'CO'
    VENTAA = 'VE'

    DEPARTAMENTO = [
    (ADMINISTRADOR, 'Administrador'),
    (LOGISTICO, 'Logistico'),
    (PRODUCTIVO, 'Productivo'),
    (CONTROLO, 'Controlo'),
    (VENTAA,  'Ventaa'),
    ]

    depar = forms.CharField(widget=forms.RadioSelect(choices=DEPARTAMENTO))

    class Meta:
        model = User
        fields = ["username", "depar", "password1", "password2"]
