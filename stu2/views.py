from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from stu.models import *


class Index_emp_add(View):
    def get(self, request, *args, **kwargs):
        department_list = DepartmentInfo.objects.filter()
        role_list = UserRole.objects.filter()
        return render(request, 'emp_add.html',{'department_list':department_list,'role_list':role_list})

    def post(self, request, *args, **kwargs):
        print(request.POST.dict())
        a = request.POST.dict()
        # 获取外键对象实例
        department_obj = DepartmentInfo.objects.get(department_id=a['department'])
        a['department'] = department_obj
        role_obj = UserRole.objects.get(role_id=a['role'])
        a['role'] = role_obj
        UserInfo.objects.create(**a)
        return HttpResponse('添加成功')