from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

MARITAL_STATUS_CHOICES = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
)


class User(AbstractUser):

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Department(models.Model):  
    
      
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name = 'Department Name')
    department_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    sub_departments = models.TextField(max_length=500, blank=True, null=True, verbose_name = 'Sub Departments')
    date_created = models.DateField(auto_now_add=True, null=True)

    class Meta:
        ordering = ("-date_created",)

    def __str__(self):
        return self.name


class Employee(models.Model):
    

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="dep")
    photo = models.ImageField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(verbose_name = 'Date of Birth')
    sex = models.CharField(choices=GENDER_CHOICES, max_length=255)
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=255, verbose_name = 'Marital Status')
    home_address = models.TextField(max_length=100, blank=True, null=True, verbose_name = 'Home Address')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name = 'Phone Number')
    next_of_kin_name = models.CharField(max_length=100, verbose_name = 'Next of Kin Name')
    next_of_kin_phone_number = models.CharField(max_length=15, verbose_name = 'Next of Kin Contact Number')
    grade = models.CharField(blank=True, null=True,max_length=255)
    salary = models.DecimalField(max_digits=12, decimal_places=2)
    qualifications = models.TextField(max_length=500, blank=True, null=True)
    medical_records = models.TextField(max_length=500, blank=True, null=True, verbose_name = 'Medical Records')
    leave_record = models.TextField(max_length=500, blank=True, null=True, verbose_name = 'first name')
    displinary_record = models.TextField(max_length=500, blank=True, null=True, verbose_name = 'first name')
    date_joined = models.DateField(auto_now_add=True, null=True, verbose_name = 'first name')
    

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
        verbose_name = "Department Manager"


    def __str__(self):
        return "{} - {}".format(self.employee, self.department)

class WeeklyPerfomanceReview(models.Model):
        
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="staff_member")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="dept")

    week_starting = models.DateField(null=True)
    week_ending = models.DateField(null=True)

    ## Work Plan 
    activity1 = models.CharField(max_length=500, verbose_name = 'Activity 1')
    work_to_be_done1 = models.CharField(max_length=500, verbose_name = 'Work To Be Done (1)')
    activity2 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Activity 2')
    work_to_be_done2 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Work To Be Done (2)')
    activity3 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Activity 3')
    work_to_be_done3 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Work To Be Done (3)')
    activity4 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Activity 4')
    work_to_be_done4 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Work To Be Done (4)')
    activity5 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Activity 5')
    work_to_be_done5 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Work To Be Done (5)')
    activity6 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Activity 6')
    work_to_be_done6 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Work To Be Done (6)')
    activity7 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Activity 7')
    work_to_be_done7 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Work To Be Done (7)')


    ## Results
    work_done1 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Work Done (Day 1)')
    evidence_of_work_done1 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Evidence of Work Done (Day 1)')
    work_done2 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Work Done (Day 2)')
    evidence_of_work_done2 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Evidence of Work Done (Day 2)')
    work_done3 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Work Done (Day 3)')
    evidence_of_work_done3 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Evidence of Work Done (Day 3)')
    work_done4 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Work Done (Day 4)')
    evidence_of_work_done4 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Evidence of Work Done (Day 4)')
    work_done5 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Work Done (Day 5)')
    evidence_of_work_done5 = models.CharField(max_length=500, blank=True, null=True, verbose_name = 'Evidence of Work Done (Day 5)')
    
    
    evaluation = models.TextField(max_length=500, blank=True, null=True, verbose_name = 'Evaluation of Work Done (RESULTS):')
    innovations = models.TextField(max_length=500, blank=True, null=True, verbose_name = 'Innovation and Initiatives for the Week')
    
    # Checking Process

    comment_by_supervisor = models.TextField(max_length=100, blank=True, null=True, verbose_name = 'Comments by immediate Supervisor')
    checked_and_approved = models.BooleanField(default=False, verbose_name = 'Checked and Approved as a true record')
    comment_by_director = models.TextField(max_length=100, blank=True, null=True, verbose_name = 'Comments by Department Director')
    comment_by_assistant_director = models.TextField(max_length=100, blank=True, null=True, verbose_name = 'Comments by Assistant Director')
   
   
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ("-created_on",)
        verbose_name = "Weekly Perfomance Review"
    def __str__(self):
        return '{} {} for the for week ending {}'.format(self.employee.user.first_name, self.employee.user.last_name, self.week_ending)

