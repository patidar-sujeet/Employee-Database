from django.contrib import admin

from ems.models import Employee, Job

# Register your models here.
# admin.site.register(Employee)
# admin.site.register(Job)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name']

