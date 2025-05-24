from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from service.models import Term
from service.models import Rent
from django.core.mail import send_mail
from django.conf import settings


#             ki mera cars wali detail booking mai aa jae


from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from service.models import booking
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
    rent=Rent.objects.all()
    


    if request.method=='GET':


        k=request.GET.get('search')
        if k :
            rent=Rent.objects.filter(adress__icontains=k)

    data={'rent': rent}

    return render(request, "rental.html", data)


def contact(request):
    success = False 

    if request.method == 'GET':
        try:
            name = request.GET.get('nam', '')   
            email = request.GET.get('email', '')
            msg = request.GET.get('msg', '')

            if name and email and msg:
                subject = f"New Contact Form Submission from {name}"
                message = f"Name: {name}\nEmail: {email}\nMessage:\n{msg}"
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = ['palayushi293@gmail.com'] 

                send_mail(subject, message, from_email, recipient_list)
                success = True

                return HttpResponseRedirect('/')

        except Exception as e:
            print("Error:", e)

    return render(request, "contact.html", {"success": success})

    
        
          



def book(request,id):
    
    rent = get_object_or_404(Rent, id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('number')
        adhar=request.POST.get('adhar')
        date=request.POST.get('date')

        book=booking(
        
            name=name,
            email=email,
            phone=phone,
            idproof=adhar,
            move_Date=date
        )
    
        
        book.save()
        

    
    return render(request, 'book.html', {'rent': rent})
def story(request):
    Servicedata = Service.objects.all().order_by('service_title')
    for a in Servicedata:
        print(a.service_title)
    data = {'Servicedata': Servicedata}  # <-- define data here, after loop
    return render(request, "story.html", data)

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

def add(request):

    if request.method=='POST':
        adress=request.POST.get('adress')
        bhk=request.POST.get('bhk')
        description=request.POST.get('description')
       

        add=Rent(
            adress=adress,
            bhk=bhk,
            description=description,
            
            
        )

        add.save()
    return render(request, 'add.html')    






    
