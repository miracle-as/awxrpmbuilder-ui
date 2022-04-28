from django import forms

class projectForm(forms.Form):
    project_name = forms.CharField(label='project name', max_length=100)