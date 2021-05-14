# Generated by Django 3.2 on 2021-05-14 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('department_number', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('sub_departments', models.CharField(blank=True, max_length=500, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('photo', models.ImageField(blank=True, max_length=255, null=True, upload_to='')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('home_address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('next_of_kin_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=255)),
                ('grade', models.CharField(blank=True, max_length=255, null=True)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced')], max_length=255)),
                ('role', models.CharField(choices=[('regular', 'regular'), ('supervisor', 'supervisor')], max_length=255)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=12)),
                ('qualifications', models.CharField(blank=True, max_length=500, null=True)),
                ('medical_records', models.CharField(blank=True, max_length=500, null=True)),
                ('next_of_kin_name', models.CharField(blank=True, max_length=100, null=True)),
                ('leave_record', models.CharField(blank=True, max_length=500, null=True)),
                ('displinary_record', models.CharField(blank=True, max_length=500, null=True)),
                ('date_joined', models.DateField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_joined',),
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
                'ordering': ('from_date',),
            },
        ),
    ]
