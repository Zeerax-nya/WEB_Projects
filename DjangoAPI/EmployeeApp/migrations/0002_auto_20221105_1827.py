# Generated by Django 3.2.4 on 2022-11-05 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Departments',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]