from django.contrib import admin
from home.models import Contact
from .models import certi
from home.models import orders
from django.contrib.auth.models import Group

admin.site.site_header = 'DEPT AI'

class certiAdmin(admin.ModelAdmin):
    list_display = ('type','name','adnum','score',)
    list_filter = ['type']



# Register your models here.
admin.site.register(Contact)
admin.site.register(certi,certiAdmin)
admin.site.register(orders)
#admin.site.unregister(Group)
