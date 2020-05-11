from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    thepassword=''
    Characters=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.GET.get("length",12))
    if request.GET.get("uppercase"):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get("numbers"):
        Characters.extend(list('1234567890'))
    if request.GET.get("specialcharacters"):
        Characters.extend(list('!@#$%^&*+_-'))      
    for x in range(length):
        thepassword+=random.choice(Characters)

    return render(request,'generator/password.html',{'password':thepassword})