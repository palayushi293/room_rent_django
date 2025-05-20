from django.contrib import admin
from service.models import Service
from service.models import Term
from service.models import Rent

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_title', 'service_description')

class ServiceTerm(admin.ModelAdmin):
    list_display=('service_title', 'service_des')


class ServiceRent(admin.ModelAdmin):
    list_display=('adress','bhk','description')    


admin.site.register(Term, ServiceTerm)
admin.site.register(Service,ServiceAdmin)    
admin.site.register(Rent,ServiceRent)
# Register your models here.



