from django.shortcuts import render
from django.views.generic import View
from myapp.models import Employee
from django.http import HttpResponse
import json

# Create your views here.
class EmployeeDetail(View):
    def get(self, *args, **kwargs):
        emp= Employee.objects.get(id=2)
        emp_data= {'name':emp.name, 'age':emp.age, 'email':emp.email, 'place':emp.place}
        json_data= json.dumps(emp_data)
        return HttpResponse(json_data, content_type= 'application/json')