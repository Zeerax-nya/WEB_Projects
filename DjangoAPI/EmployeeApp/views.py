from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # дает другим domains access к API-methods
from rest_framework.parsers import JSONParser        # для парсинга входящей инфы в DATA-MODULE (+ниже строка)
from django.http.response import JsonResponse

# импротируем наши созданные модули и сериалайзеры:
from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer
# хранилище файлов на уровне django:
from django.core.files.storage import default_storage

# Create your views here.
# создаем API методы для Department:
@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)  # переформатируем в JSON-формат
        return JsonResponse(departments_serializer.data,safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DEPARTMENT_ID=department_data['DEPARTMENT_ID'])
        departments_serializer=DepartmentSerializer(department,data=department_data)
        if departments_serializer.is_valid():                               # если модуль valid -> сохр. в DB
            departments_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        department=Departments.objects.get(DEPARTMENT_ID=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)

# создаем API методы для Employees:
@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EMPLOYEE_ID=employee_data['EMPLOYEE_ID'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees.objects.get(EMPLOYEE_ID=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)

# При методе POST для файла будем задавать название, как file
@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)