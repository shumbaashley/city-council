from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .models import Department, Employee, User, WeeklyPerfomanceReview

from django.contrib.auth.models import Group

admin.site.unregister(Group)

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name', 'email', 'is_staff')


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    prepopulated_fields = {'username': ('first_name' , 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'is_staff',  'password1', 'password2', ),
        }),
    )


# Re-register UserAdmin
# admin.site.unregister(User)


@admin.register(User, UserAdmin)
class User(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "username", "email", "is_staff",)
    list_display_links = ("username",)
    search_fields = ("username", "email", "first_name", "last_name")


# admin.site.register(UserAdmin)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "department_number", "sub_departments",)

@admin.register(Employee)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ("user" , "works_number", "department", "sex",  "phone_number", "date_joined",)
    list_display_links = ("user", "department")
    # list_filter = ("user", "department","date_joined",)
    search_fields = ("user", "works_number", "department",)


# @admin.register(DepartmentManager)
# class DepartmentManagerAdmin(admin.ModelAdmin):
#     list_display = ("employee", "department", "from_date", "to_date")


@admin.register(WeeklyPerfomanceReview)
class WeeklyPerfomanceReview(admin.ModelAdmin):
    list_display = ("employee", "department", "week_starting", "week_ending", "checked_and_approved", "created_on")
    list_display_links = ("employee", "department",)
    # list_filter = ("employee", "department",  "checked_and_approved", "week_starting", "week_ending",)
    search_fields = ("employee", "department",)