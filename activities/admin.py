from django.contrib import admin

# Register your models here.
from .models import  WeeklyPerfomanceReview


# admin.site.register(WeeklyPerfomanceReview)


@admin.register(WeeklyPerfomanceReview)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("employee", "week_starting", "created_on")
