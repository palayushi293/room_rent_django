from django.contrib import admin
from service.models import Service
from service.models import Term
from service.models import Rent
from service.models import booking
class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_title', 'service_description')

class ServiceTerm(admin.ModelAdmin):
    list_display=('service_title', 'service_des')


class ServiceRent(admin.ModelAdmin):
    list_display=('adress','bhk','description')    

class Servicebooking(admin.ModelAdmin):
    list_display=('name','phone','email','idproof','move_Date')

admin.site.register(Term, ServiceTerm)
admin.site.register(Service,ServiceAdmin)    
admin.site.register(Rent,ServiceRent)
admin.site.register(booking,Servicebooking)

# Register your models here.



