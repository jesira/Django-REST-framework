from django.contrib import admin
from .models import Employee, Owner


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'emp_id', 'is_deleted')
    list_editable = ['is_deleted']
    list_filter = ['is_deleted']


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'owner_id', 'is_deleted')
    list_editable = ['is_deleted']
    list_filter = ['is_deleted']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Owner, OwnerAdmin)
