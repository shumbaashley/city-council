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
