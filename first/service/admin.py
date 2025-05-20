from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_title', 'service_description')


admin.site.register(Service,ServiceAdmin)    
# Register your models here.
