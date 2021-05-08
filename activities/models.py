# from django.db import models
# import uuid
# from council.models import Employee

# # Create your models here.


# class WorkPlan(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
#     employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name="employee")
#     activities = models.CharField(max_length=500, blank=True, null=True)
#     work_to_be_done = models.CharField(max_length=500, blank=True, null=True)
#     week_starting = models.DateField(null=True)
#     week_ending = models.DateField(null=True)
#     created_on = models.DateTimeField(auto_now_add=True, null=True)
    

#     class Meta:
#         ordering = ("created_on",)

#     def __str__(self):
#         return 'Work plan for {} {} in the week starting {}'.format(self.employee.user.first_name, self.employee.user.last_name, self.week_starting)

# class WorkPerformance(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
#     work_plan = models.OneToOneField(WorkPlan, on_delete=models.CASCADE, related_name="plan")
#     work_done = models.CharField(max_length=500, blank=True, null=True)
#     evidence_of_work_done = models.CharField(max_length=500, blank=True, null=True)
#     created_on = models.DateTimeField(auto_now_add=True, null=True)
    

#     class Meta:
#         ordering = ("created_on",)

#     def __str__(self):
#         return 'Work results for {} {} according to the work plan for week starting {}'.format(self.work_plan.employee.user.first_name, self.work_plan.employee.user.last_name, self.work_plan.week_starting)


# class PerfomanceReview(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
#     work_performance = models.OneToOneField(WorkPerformance, on_delete=models.CASCADE, related_name="performance")
#     comment_by_supervisor = models.CharField(max_length=100, blank=True, null=True)
#     comment_by_director = models.CharField(max_length=100, blank=True, null=True)
#     created_on = models.DateTimeField(auto_now_add=True, null=True)
    

#     class Meta:
#         ordering = ("created_on",)

#     def __str__(self):
#         return 'Performance Review for {} {} on week ending {}'.format(self.work_results.work_plan.employee.user.first_name, self.work_results.work_plan.employee.user.last_name, self.work_results.work_plan.week_ending)




from django.db import models

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True, help_text='Use the format DD/MM/YYYY')

    def __str__(self):
        return self.name
