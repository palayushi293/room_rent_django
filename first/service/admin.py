from django.contrib import admin
from service.models import Service
from service.models import Term

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_title', 'service_description')

class ServiceTerm(admin.ModelAdmin):
    list_display=('service_title', 'service_des')


admin.site.register(Term, ServiceTerm)
admin.site.register(Service,ServiceAdmin)    
# Register your models here.



