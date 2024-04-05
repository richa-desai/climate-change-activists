''' module docstring '''
from datetime import datetime
from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    ''' try '''
    # return HttpResponse("hommepage")
    context = {
        "variable": "this is sent"
    }
    # messages.success(request, "this is a test msg")
    return render(request, 'index.html', context)

def aboutus(request):
    ''' try '''
    return render(request, 'about.html')

def contactus(request):
    ''' try '''
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")

    return render(request, 'contact.html')
