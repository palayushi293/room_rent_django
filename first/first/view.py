from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render # type: ignore

from django.core.mail import send_mail
from django.conf import settings


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
    success = False  # Ensure 'success' is always defined

    if request.method == 'GET':
        try:
            name = request.GET.get('nam', '')   # Make sure your input field is named 'nam'
            email = request.GET.get('email', '')
            msg = request.GET.get('msg', '')

            if name and email and msg:
                subject = f"New Contact Form Submission from {name}"
                message = f"Name: {name}\nEmail: {email}\nMessage:\n{msg}"
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = ['palayushi293@gmail.com']  # ✅ Corrected email

                send_mail(subject, message, from_email, recipient_list)
                success = True

                return HttpResponseRedirect('/')

        except Exception as e:
            print("Error:", e)

    return render(request, "contact.html", {"success": success})

    
        
          



def book(request):
    return render(request, "book.html")

def story(request):
    return render(request, "story.html")