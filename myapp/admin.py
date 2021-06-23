from django.contrib import admin

# Register your models here.
from myapp.models import *

class StudentAdmin(admin.ModelAdmin):
    fields = (('name','age'), 'roll') 
    list_display = ("name", "age", 'show_name')
    list_filter = ("age", )
    search_fields = ("name", )

    def show_name(self, obj):
        from django.utils.html import format_html
        result = Students.objects.filter(name= obj)
        # return  result[0].name
        return format_html('<a href="https://www.google.com/">{}</a>', result[0].name)

    # fieldsets = (
    #     (
    #         None, {'fields' :(('name','age'), 'roll')}
    #     ),
    # )
    # @admin.display(empty_value='???')
    # def fullname(self):
    #     return obj.name 


        

admin.site.register(Students, StudentAdmin)
admin.site.site_header = "My Cool Admin Pannel"
# admin.site.index_title = "Welcome to Devnote Tutorial"