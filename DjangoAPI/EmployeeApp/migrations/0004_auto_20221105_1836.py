# Generated by Django 3.2.4 on 2022-11-05 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0003_departments_employees'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Departments',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]
