from django.db import models
import uuid
from council.models import Employee
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class WeeklyPerfomanceReview(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    
    
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="employee")

    week_starting = models.DateField(null=True)
    week_ending = models.DateField(null=True)

    ## Work Plan 
    activity1 = models.CharField(max_length=500, blank=True, null=True)
    activity2 = models.CharField(max_length=500, blank=True, null=True)
    activity3 = models.CharField(max_length=500, blank=True, null=True)
    activity4 = models.CharField(max_length=500, blank=True, null=True)
    activity5 = models.CharField(max_length=500, blank=True, null=True)
    activity6 = models.CharField(max_length=500, blank=True, null=True)
    activity7 = models.CharField(max_length=500, blank=True, null=True)
    work_to_be_done1 = models.CharField(max_length=500, blank=True, null=True)
    work_to_be_done2 = models.CharField(max_length=500, blank=True, null=True)
    work_to_be_done3 = models.CharField(max_length=500, blank=True, null=True)
    work_to_be_done4 = models.CharField(max_length=500, blank=True, null=True)
    work_to_be_done5 = models.CharField(max_length=500, blank=True, null=True)
    work_to_be_done6 = models.CharField(max_length=500, blank=True, null=True)
    work_to_be_done7 = models.CharField(max_length=500, blank=True, null=True)


    ## Results
    work_done1 = models.CharField(max_length=500, blank=True, null=True)
    work_done2 = models.CharField(max_length=500, blank=True, null=True)
    work_done3 = models.CharField(max_length=500, blank=True, null=True)
    work_done4 = models.CharField(max_length=500, blank=True, null=True)
    work_done5 = models.CharField(max_length=500, blank=True, null=True)
    evidence_of_work_done1 = models.CharField(max_length=500, blank=True, null=True)
    evidence_of_work_done2 = models.CharField(max_length=500, blank=True, null=True)
    evidence_of_work_done3 = models.CharField(max_length=500, blank=True, null=True)
    evidence_of_work_done4 = models.CharField(max_length=500, blank=True, null=True)
    evidence_of_work_done5 = models.CharField(max_length=500, blank=True, null=True)
    evaluation = models.CharField(max_length=500, blank=True, null=True)
    innovations = models.CharField(max_length=500, blank=True, null=True)
    
    
    supervisors = models.ManyToManyField(Employee, related_name="superiors")

    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ("created_on",)

    def __str__(self):
        return 'Work results for {} {} according to the work plan for week starting {}'.format(self.work_plan.employee.user.first_name, self.work_plan.employee.user.last_name, self.work_plan.week_starting)


class PerfomanceReview(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    work_performance = models.OneToOneField(WeeklyPerfomanceReview, on_delete=models.CASCADE, related_name="performance")
    comment_by_supervisor = models.CharField(max_length=100, blank=True, null=True)
    checked_and_approved = models.BooleanField(default=False)
    comment_by_director = models.CharField(max_length=100, blank=True, null=True)
    comment_by_assistant_director = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    

    class Meta:
        ordering = ("created_on",)

    def __str__(self):
        return 'Performance Review for {} {} on week ending {}'.format(self.work_results.work_plan.employee.user.first_name, self.work_results.work_plan.employee.user.last_name, self.work_results.work_plan.week_ending)




# from django.db import models

# TITLE_CHOICES = [
#     ('MR', 'Mr.'),
#     ('MRS', 'Mrs.'),
#     ('MS', 'Ms.'),
# ]

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=3, choices=TITLE_CHOICES)
#     birth_date = models.DateField(blank=True, null=True, help_text='Use the format DD/MM/YYYY')

#     def __str__(self):
#         return self.name
