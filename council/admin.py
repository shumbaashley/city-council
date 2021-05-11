from django.contrib import admin

from .models import Department, Employee, DepartmentManager


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "department_number", "sub_departments", "date_created")

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("user", "photo",  "sex",  "phone_number", "salary", "home_address", "date_joined", "next_of_kin_name", "next_of_kin_phone_number")



@admin.register(DepartmentManager)
class DepartmentManagerAdmin(admin.ModelAdmin):
    list_display = ("employee", "department", "from_date", "to_date")

