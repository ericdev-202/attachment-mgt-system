from django.contrib import admin
from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import Staff,Student,Elogbook,Document,StudentDetails,Lecturer,CompDetails

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User 
# Register your models here.

class UserAdminConfig(UserAdmin):
    list_display=['email','username','first_name','date_of_birth','city']
    search_fields=['email','username','city']
    readonly_fields=['date_joined','last_login']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','first_name','last_name','date_of_birth','city')}),
        ('Activity', {'fields': ('date_joined','last_login')}),
        ('Permissions', {'fields': ('is_admin','is_active','is_staff','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name', 'date_of_birth','city', 'password1', 'password2'),
        }),
    )

# admin.site.register(User,UserAdminConfig)
admin.site.register(User)
admin.site.register(Staff)
admin.site.register(StudentDetails)
admin.site.register(Student)
admin.site.register(Document)
admin.site.register(Lecturer)
admin.site.register(Elogbook)
admin.site.register(CompDetails)

# Register your models here.
