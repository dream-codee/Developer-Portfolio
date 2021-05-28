from django.shortcuts import render

# Create your views here.
name = "SABA DANISH"
email = "sabaminhaj.python@gmail.com"
phno = 9123123123
Organizations= "Virtual Intership with Accenture,Internship in Tequed Labs on AI"
Achievements="Certificate from Accenture,Certificates From Microsoft,Certificate from Uipath on its way to join my Portfolio"

def index(request):
    return render(request, "Employeehomepage.html", {'name': name})


def profile_pic(request):
    return render(request, "pic.html", {'name': name})


def profile(request):
    return render(request, "portfolio.html", {"name": name, "email": email, "phno": phno})

def organizations(request):
    return render(request ,"organizations.html",{"Organizations" : Organizations})

def achievements(request):
    return render(request,"achievements.html",{"Achievements" : Achievements})