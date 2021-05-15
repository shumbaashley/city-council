from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .models import Department, Employee, DepartmentManager, User, WeeklyPerfomanceReview

from django.contrib.auth.models import Group

admin.site.unregister(Group)

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name' , 'last_name', 'email')


class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    prepopulated_fields = {'username': ('first_name' , 'last_name', )}

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email',  'password1', 'password2', ),
        }),
    )


# Re-register UserAdmin
# admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "department_number", "sub_departments", "date_created")

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("user", "photo",  "sex",  "phone_number", "salary", "home_address", "date_joined", "next_of_kin_name", "next_of_kin_phone_number")



@admin.register(DepartmentManager)
class DepartmentManagerAdmin(admin.ModelAdmin):
    list_display = ("employee", "department", "from_date", "to_date")


@admin.register(WeeklyPerfomanceReview)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("employee",  "week_starting", "week_ending", "created_on")
