from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=280)
    phone = forms.CharField(max_length=280)
