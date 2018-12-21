#coding=utf-8
from django.http import  HttpResponseRedirect
from django.shortcuts import render
from stu.models import *
# Create your views here.
def dept_add(request):
    if request.method=='GET':
        return render(request,'dept_add.html')
    else:
        departmentName=request.POST.get('departmentName','')
        departmentDesc=request.POST.get('departmentDesc','')
        departmentNamelist=DepartmentInfo.objects.filter(department_name=departmentName)
        print(departmentNamelist)
        if departmentNamelist:
            return HttpResponseRedirect('/stu1/dept_list/')
        else:
            DepartmentInfo.objects.create(department_name=departmentName, department_desc=departmentDesc, is_used=1)
            return HttpResponseRedirect('/stu1/dept_list/')

