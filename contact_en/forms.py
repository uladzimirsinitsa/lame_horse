from django import forms
from .models import Contact_en

class ContactForm_en(forms.ModelForm):

	class Meta:
		model = Contact_en
		fields = ('subject', 'email', 'message',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['subject'].widget.attrs.update({'class': 'form-control'})
		self.fields['email'].widget.attrs.update({'class': 'form-control'})
		self.fields['message'].widget.attrs.update({'class': 'form-control'})