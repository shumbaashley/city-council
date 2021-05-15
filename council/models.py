from django.db import models
import uuid
from django.contrib.auth.models import User


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

MARITAL_STATUS_CHOICES = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
)



class Department(models.Model):  
    
      
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    department_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    sub_departments = models.CharField(max_length=500, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self):
        return self.name


class Employee(models.Model):
    

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    photo = models.ImageField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    home_address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    next_of_kin_phone_number = models.CharField(max_length=15,)
    sex = models.CharField(choices=GENDER_CHOICES, max_length=255)
    grade = models.CharField(blank=True, null=True,max_length=255)
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=255)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    qualifications = models.CharField(max_length=500, blank=True, null=True)
    medical_records = models.CharField(max_length=500, blank=True, null=True)
    next_of_kin_name = models.CharField(max_length=100,)
    leave_record = models.CharField(max_length=500, blank=True, null=True)
    displinary_record = models.CharField(max_length=500, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True, null=True)
    

    class Meta:
        ordering = ("-date_joined",)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class DepartmentManager(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="worker")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="field")
    from_date = models.DateField(auto_now_add=True, null=True)
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ("-from_date",)

    def __str__(self):
        return "{} - {}".format(self.employee, self.department)

class WeeklyPerfomanceReview(models.Model):
        
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="staff_member")

    week_starting = models.DateField(null=True)
    week_ending = models.DateField(null=True)

    ## Work Plan 
    activity1 = models.CharField(max_length=500)
    activity2 = models.CharField(max_length=500, blank=True, null=True)
    activity3 = models.CharField(max_length=500, blank=True, null=True)
    activity4 = models.CharField(max_length=500, blank=True, null=True)
    activity5 = models.CharField(max_length=500, blank=True, null=True)
    activity6 = models.CharField(max_length=500, blank=True, null=True)
    activity7 = models.CharField(max_length=500, blank=True, null=True)
    work_to_be_done1 = models.CharField(max_length=500)
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
    
    
    # supervisors = models.ManyToManyField(Employee, related_name="superiors")

    created_on = models.DateTimeField(auto_now_add=True, null=True)

    comment_by_supervisor = models.CharField(max_length=100, blank=True, null=True)
    checked_and_approved = models.BooleanField(default=False)
    comment_by_director = models.CharField(max_length=100, blank=True, null=True)
    comment_by_assistant_director = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ("-created_on",)

    def __str__(self):
        return '{} {} for the for week ending {}'.format(self.employee.user.first_name, self.employee.user.last_name, self.week_ending)

