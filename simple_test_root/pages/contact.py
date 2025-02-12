# /simple_test_root/pages/contact.py
from django import forms

# ContactForm class for handling contact information
class ContactForm(forms.Form):
	your_name = forms.CharField(max_length=100, label='Your name')
	email = forms.EmailField(required=False,label='Your e-mail address')
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)