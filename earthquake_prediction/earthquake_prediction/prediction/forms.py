from django import forms


class DepthPredictionForm(forms.Form):
    Year = forms.IntegerField()
    Month = forms.IntegerField()
    Day = forms.IntegerField()
    Hour = forms.IntegerField()
    Minutes = forms.IntegerField()
    Latitude = forms.FloatField()
    Longitude = forms.FloatField()
    Magnitude = forms.FloatField()
