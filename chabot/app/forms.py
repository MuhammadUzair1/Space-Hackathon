from django import forms

class GenerateTextForm(forms.Form):
    prompt = forms.CharField(label='Enter a prompt', max_length=200)
