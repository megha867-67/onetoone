from django import forms
class CountryCapitalForm(forms.Form):
 countryname = forms.CharField(max_length=100,label="CountryName")
 capitalname = forms.CharField(max_length=100,label="CapitalName")