from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render # type: ignore
from service.models import Term
from django.core.mail import send_mail
from django.conf import settings

from service.models import Service


def aboutUs(request):
    return HttpResponse("welcone")


def home(request):
    term=Term.objects.all()
    data={
        'title':'Home Page',
        'term':term
        
        
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

    Servicedata=Service.objects.all().order_by('service_title') # for descending ('-service_title')
    #Servicedata=Service.objects.all().order_by('service_title')[:3] for limit
    for a in Servicedata:
        print(a.service_title)
        data={'Servicedata': Servicedata}
    return render(request, "story.html",data)


def marks(request):
    if request.method=='GET':
        one =int(request.GET.get('sub1', 0))
        two=int(request.GET.get('sub2' ,0))
        three=int(request.GET.get('sub3', 0))
        ans=((one+two+three)/300)*100
        if ans>=80:
            p="a+"
        elif ans<80 and ans>20:
            p="b"
        else:
            p="fail"    


        data={'output':ans, 'grade': p}

    return render(request,'marks.html', data)
    return HttpResponseRedirect('/')



    
