from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mysite/index.html', {})

def contact(request):
    return render(request, 'mysite/contact.html', {})

def about(request):
    return render(request, 'mysite/about.html', {})
