from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'emp_id')


admin.site.register(Employee, EmployeeAdmin)
