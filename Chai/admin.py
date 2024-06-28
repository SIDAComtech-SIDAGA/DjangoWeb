from django.contrib import admin
from .models import Chai

# Register your models here

class ChaiAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity','image')


admin.site.register(Chai,ChaiAdmin)