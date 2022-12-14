# Generated by Django 3.2.4 on 2021-06-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DEPARTMENT_ID', models.AutoField(primary_key=True, serialize=False)),
                ('DEPARTMENT_NAME', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EMPLOYEE_ID', models.AutoField(primary_key=True, serialize=False)),
                ('EMPLOYEE_NAME', models.CharField(max_length=500)),
                ('DEPARTMENT', models.CharField(max_length=500)),
                ('DATE_OF_JOINING', models.DateField()),
                ('PHOTO_FILE_NAME', models.CharField(max_length=500)),
            ],
        ),
    ]
