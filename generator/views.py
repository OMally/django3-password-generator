from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    #return HttpResponse("Hello there friend!")
    return render(request, "generator/home.html", {"password":"dhkfsoskls45"})

def password(request):
    #return HttpResponse("<h1>Eggs are so good!</h1>")

    chars = list("lavcekfgjituprswhomniyzxwqdb")
    #length = 10
    if request.GET.get("uppercase"):
        chars.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("numbers"):
        chars.extend(list("012345678901234567890123456789"))

    if request.GET.get("special"):
        chars.extend(list("@*$)!%$:;)',.?<>"))

    pwd_length = int(request.GET.get("length",8))      #The name "length" is defined in the home.html file
    thepwd = ""
    for x in range(pwd_length):
        thepwd += random.choice(chars)
    return render(request, "generator/password.html", {"password": thepwd})

def about(request):
    return render(request, "generator/about.html")