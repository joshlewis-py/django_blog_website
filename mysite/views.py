from django.shortcuts import render
from django.http import HttpResponse # Add this
from django.views.generic import View
from .forms import ContactForm # Add this
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'mysite/index.html', {})

def about(request):
    return render(request, 'mysite/about.html', {})

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['ENTER EMAIL HERE'])

            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'mysite/contact_us.html', {'form': form})
