from django.db import models

# Create your models here.
# Создаем модели (таблицы в sql) на уровне django. Необходим serializer для перевода их типа в JSON

class Departments(models.Model):
    DEPARTMENT_ID = models.AutoField(primary_key=True)
    DEPARTMENT_NAME = models.CharField(max_length=500)

class Employees(models.Model):
    EMPLOYEE_ID = models.AutoField(primary_key=True)
    EMPLOYEE_NAME = models.CharField(max_length=500)
    DEPARTMENT = models.CharField(max_length=500)
    DATE_OF_JOINING = models.DateField()
    PHOTO_FILE_NAME = models.CharField(max_length=500)