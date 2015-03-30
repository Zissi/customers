from django import forms

class MailForm(forms.Form):
    subject = forms.CharField(label='subject', max_length=100)
    text = forms.CharField(label='text', max_length=1000)