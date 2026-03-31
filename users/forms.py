from django import forms
from .models import UserModel

class UserForm(forms.Form):
	name = forms.CharField(max_length=100, required=True, label='Name')
	age = forms.IntegerField(required=True, label='Age')
	job = forms.ChoiceField(required=True, label='Job', choices=[
		(1, 'Site Reliability Engineer'),
		(2, 'Developer'),
		(3, 'Manager'),
		(4, 'Director'),
	])

class UserModelForm(forms.ModelForm):
	class Meta:
		model = UserModel
		fields = ['name','age','job']