from django import forms

class home_forms(forms.Form):
	first_name = forms.CharField(max_length = 30)
	second_name = forms.CharField(max_length = 30)
	email = forms.EmailField(max_length = 30)
