from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import ContactForm_en
from django.core.mail import send_mail


def contact_en(request):
	template = 'contact_en/contact.html'
	if request.method == 'POST':
		form = ContactForm_en(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject'] + '-' + form.cleaned_data['email']
			message = form.cleaned_data['message']
			email = form.cleaned_data['email']
			send_mail(subject, message, email, ['gobcasinos@gmail.com'], fail_silently=False)
			return HttpResponseRedirect('/')
	else:
		form = ContactForm_en()
	context = {
		'form': form
	}
	return render(request, template, context)
