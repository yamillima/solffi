from django import forms
from django.forms import TextInput
from .models import Cliente, Inversionista


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('monto', 'nombre', 'email', 'whatsapp', 'ciudad')

        widgets = {
            'monto': TextInput(attrs={'placeholder': '¿Cuánto necesitas en pesos?'}),
            'nombre': TextInput(attrs={'placeholder': 'Nombre completo'}),
            'email': TextInput(attrs={'placeholder': 'Correo electrónico'}),
            'whatsapp': TextInput(attrs={'placeholder': 'Número de WhatsApp'}),
            'ciudad': TextInput(attrs={'placeholder': 'Ciudad o municipio'}),
        }


class InversionistaForm(forms.ModelForm):

    class Meta:
        model = Inversionista
        fields = ('monto', 'nombre', 'email', 'whatsapp', 'ciudad')

        widgets = {
            'monto': TextInput(attrs={'placeholder': '¿Cuánto quieres invertir en pesos?'}),
            'nombre': TextInput(attrs={'placeholder': 'Nombre completo'}),
            'email': TextInput(attrs={'placeholder': 'Correo electrónico'}),
            'whatsapp': TextInput(attrs={'placeholder': 'Número de WhatsApp'}),
            'ciudad': TextInput(attrs={'placeholder': 'Ciudad o municipio'}),
        }
