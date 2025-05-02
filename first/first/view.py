from django.http import HttpResponse
from django.shortcuts import render # type: ignore


def aboutUs(request):
    return HttpResponse("welcone")


def home(request):
    data={
        'title':'Home Page'
        
    }
    return render(request,"index.html",data)


def rentals(request):
    return render(request, "rental.html")


def contact(request):
    return render(request, "contact.html")

def book(request):
    return render(request, "book.html")

def story(request):
    return render(request, "story.html")