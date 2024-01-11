from django.contrib import admin

# Register your models here.

from app.models import *




class customize(admin.ModelAdmin):
    list_display=['Sname','Sage','Smobile','Alternative_mobile']
    list_display_links=['Smobile']
    list_editable=['Sname']
    list_per_page=1
    

admin.site.register(Student,customize)
