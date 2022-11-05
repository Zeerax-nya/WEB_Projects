from rest_framework import serializers
from EmployeeApp.models import Departments,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DEPARTMENT_ID','DEPARTMENT_NAME')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EMPLOYEE_ID','EMPLOYEE_NAME','DEPARTMENT','DATE_OF_JOINING','PHOTO_FILE_NAME')