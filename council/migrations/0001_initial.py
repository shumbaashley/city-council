# Generated by Django 3.2.3 on 2021-05-29 09:28

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Department Name')),
                ('department_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('sub_departments', models.TextField(blank=True, max_length=500, null=True, verbose_name='Sub Departments')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Department Manager',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photo', models.ImageField(blank=True, max_length=255, null=True, upload_to='')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=255)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced')], max_length=255, verbose_name='Marital Status')),
                ('home_address', models.TextField(blank=True, max_length=100, null=True, verbose_name='Home Address')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('next_of_kin_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Next of Kin Name')),
                ('next_of_kin_phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Next of Kin Contact Number')),
                ('grade', models.CharField(blank=True, max_length=255, null=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=12)),
                ('qualifications', models.TextField(blank=True, max_length=500, null=True)),
                ('medical_records', models.TextField(blank=True, max_length=500, null=True, verbose_name='Medical Records')),
                ('leave_record', models.TextField(blank=True, max_length=500, null=True, verbose_name='Leave Record')),
                ('displinary_record', models.TextField(blank=True, max_length=500, null=True, verbose_name='Displinary Record')),
                ('date_joined', models.DateField(auto_now_add=True, null=True)),
                ('works_number', models.CharField(max_length=15, verbose_name='Works Number')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dep', to='council.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL, verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Employee Profile',
                'verbose_name_plural': 'Employee Profiles',
                'ordering': ('-date_joined',),
            },
        ),
        migrations.CreateModel(
            name='WeeklyPerfomanceReview',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('week_starting', models.DateField(null=True)),
                ('week_ending', models.DateField(null=True)),
                ('activity1', models.CharField(max_length=500, verbose_name='Activity 1')),
                ('work_to_be_done1', models.CharField(max_length=500, verbose_name='Work To Be Done (1)')),
                ('activity2', models.CharField(blank=True, max_length=500, null=True, verbose_name='Activity 2')),
                ('work_to_be_done2', models.CharField(blank=True, max_length=500, null=True, verbose_name='Work To Be Done (2)')),
                ('activity3', models.CharField(blank=True, max_length=500, null=True, verbose_name='Activity 3')),
                ('work_to_be_done3', models.CharField(blank=True, max_length=500, null=True, verbose_name='Work To Be Done (3)')),
                ('activity4', models.CharField(blank=True, max_length=500, null=True, verbose_name='Activity 4')),
                ('work_to_be_done4', models.CharField(blank=True, max_length=500, null=True, verbose_name='Work To Be Done (4)')),
                ('activity5', models.CharField(blank=True, max_length=500, null=True, verbose_name='Activity 5')),
                ('work_to_be_done5', models.CharField(blank=True, max_length=500, null=True, verbose_name='Work To Be Done (5)')),
                ('activity6', models.CharField(blank=True, max_length=500, null=True, verbose_name='Activity 6')),
                ('work_to_be_done6', models.CharField(blank=True, max_length=500, null=True, verbose_name='Work To Be Done (6)')),
                ('activity7', models.CharField(blank=True, max_length=500, null=True, verbose_name='Activity 7')),
                ('work_to_be_done7', models.CharField(blank=True, max_length=500, null=True, verbose_name='Work To Be Done (7)')),
                ('work_done1', models.CharField(blank=True, max_length=500, null=True, verbose_name='Work Done (Day 1)')),
                ('evidence_of_work_done1', models.CharField(blank=True, max_length=500, null=True, verbose_name='Evidence of Work Done (Day 1)')),
                ('work_done2', models.CharField(blank=True, max_length=500, null=True, verbose_name='Work Done (Day 2)')),
                ('evidence_of_work_done2', models.CharField(blank=True, max_length=500, null=True, verbose_name='Evidence of Work Done (Day 2)')),
                ('work_done3', models.CharField(blank=True, max_length=500, null=True, verbose_name='Work Done (Day 3)')),
                ('evidence_of_work_done3', models.CharField(blank=True, max_length=500, null=True, verbose_name='Evidence of Work Done (Day 3)')),
                ('work_done4', models.CharField(blank=True, max_length=500, null=True, verbose_name='Work Done (Day 4)')),
                ('evidence_of_work_done4', models.CharField(blank=True, max_length=500, null=True, verbose_name='Evidence of Work Done (Day 4)')),
                ('work_done5', models.CharField(blank=True, max_length=500, null=True, verbose_name='Work Done (Day 5)')),
                ('evidence_of_work_done5', models.CharField(blank=True, max_length=500, null=True, verbose_name='Evidence of Work Done (Day 5)')),
                ('evaluation', models.TextField(blank=True, max_length=500, null=True, verbose_name='Evaluation of Work Done (RESULTS):')),
                ('innovations', models.TextField(blank=True, max_length=500, null=True, verbose_name='Innovation and Initiatives for the Week')),
                ('comment_by_supervisor', models.TextField(blank=True, max_length=100, null=True, verbose_name='Comments by immediate Supervisor')),
                ('checked_and_approved', models.BooleanField(default=False, verbose_name='Checked and Approved as a true record')),
                ('comment_by_director', models.TextField(blank=True, max_length=100, null=True, verbose_name='Comments by Department Director')),
                ('comment_by_assistant_director', models.TextField(blank=True, max_length=100, null=True, verbose_name='Comments by Assistant Director')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dept', to='council.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_member', to='council.employee')),
            ],
            options={
                'verbose_name': 'Weekly Perfomance Review',
                'verbose_name_plural': 'Weekly Perfomance Reviews',
                'ordering': ('-created_on',),
            },
        ),
        migrations.CreateModel(
            name='DepartmentManager',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('from_date', models.DateField(auto_now_add=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field', to='council.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker', to='council.employee')),
            ],
            options={
                'verbose_name': 'Department Manager',
                'verbose_name_plural': 'Department Managers',
                'ordering': ('-from_date',),
            },
        ),
    ]
