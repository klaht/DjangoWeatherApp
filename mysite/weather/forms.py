from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='City name', max_length=50)

