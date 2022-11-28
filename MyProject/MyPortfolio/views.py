from email import message
import imp
from re import sub
from django.shortcuts import render
from django.http import HttpResponse
from .models import Info

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        info = Info()
        info.name = request.POST.get("name")
        info.email = request.POST.get("email")
        info.subject = request.POST.get("subject")
        info.message = request.POST.get("message")
        
        info.save()
        
    return render(request, 'contact.html')

def showdata(request):
    infos = Info.objects.all()
    #for i in infos:
        #print(i.id, i.name, i.email, i.subject, i.message)
    data = {'Info' : infos}
    
    return render(request, 'data.html', data)