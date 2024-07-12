from django import forms

class FigureForm(forms.Form):
    figure = forms.IntegerField(label='Enter figure', min_value=1, max_value=99999999999)
