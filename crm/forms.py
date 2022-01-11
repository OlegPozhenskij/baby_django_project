from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=280, required=False)
    phone = forms.CharField(max_length=280)
