from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from stu.models import *


class Index_emp_list(View):
    def get(self, request, *args, **kwargs):
        user_info = UserInfo.objects.filter()
        listlength = user_info.count()
        return render(request,'emp_list.html',{'user_info':user_info,'listlength':listlength})
    def post(self,request,*args,**kwargs):
        # 读取数据库customer_info信息
        info = request.POST.get('info')
        type = int(request.POST.get('type'))
        department_name_list = []
        role_name_list = []
        if type==1:
            user_info = UserInfo.objects.filter(user_name=info)
            for ui in user_info:
                department_name_list.append(ui.department.department_name)
                role_name_list.append(ui.role.role_name)
            juser_info = serializers.serialize('json',user_info)
            return JsonResponse({'user_info': juser_info,'department_name_list':department_name_list,'role_name_list':role_name_list})
        elif type==2:
            user_info = UserInfo.objects.filter(department__department_name=info)
            for ui in user_info:
                department_name_list.append(ui.department.department_name)
                role_name_list.append(ui.role.role_name)
            juser_info = serializers.serialize('json', user_info)
            return JsonResponse({'user_info': juser_info, 'department_name_list': department_name_list,
                                 'role_name_list': role_name_list})
        elif type==3:
            user_info = UserInfo.objects.filter(role__role_name=info)
            for ui in user_info:
                department_name_list.append(ui.department.department_name)
                role_name_list.append(ui.role.role_name)
            juser_info = serializers.serialize('json', user_info)
            return JsonResponse({'user_info': juser_info, 'department_name_list': department_name_list,
                                 'role_name_list': role_name_list})
        elif type==4:
            user_info = UserInfo.objects.filter(user_diploma=info)
            for ui in user_info:
                department_name_list.append(ui.department.department_name)
                role_name_list.append(ui.role.role_name)
            juser_info = serializers.serialize('json', user_info)
            return JsonResponse({'user_info': juser_info, 'department_name_list': department_name_list,
                                 'role_name_list': role_name_list})


class Index_emp_edit(View):
    def get(self, request, *args, **kwargs):
        un = request.GET.get('un')
        un_obj = UserInfo.objects.get(user_name=un)
        return render(request, 'emp_edit.html',{'un_obj':un_obj})

    def post(self, request, *args, **kwargs):
        a = request.POST.dict()
        # 获取外键对象实例
        department_obj = DepartmentInfo.objects.get(department_id=a['department'])
        a['department'] = department_obj
        a.pop('user_id')
        UserInfo.objects.filter(user_name=a['user_name']).update(**a)
        return HttpResponse('修改成功')


class Index_emp_detail(View):
    def get(self, request, *args, **kwargs):
        un = request.GET.get('un')
        un_obj = UserInfo.objects.get(user_name=un)
        return render(request, 'emp_detail.html', {'un_obj': un_obj})


class Index_emp_delete(View):
    def get(self, request, *args, **kwargs):
        un = request.GET.get('un')
        UserInfo.objects.get(user_name=un).delete()
        return HttpResponse('删除成功')


class Index_house_list(View):
    def get(self, request, *args, **kwargs):
        house_info = HouseInfo.objects.filter()
        listlength = house_info.count()
        return render(request,'house_list.html',{'house_info':house_info,'listlength':listlength})
    def post(self,request,*args,**kwargs):
        # 读取数据库customer_info信息
        info = request.POST.get('info')
        type = int(request.POST.get('type'))
        type_name_list = []
        user_name_list = []
        if type==1:
            house_info = HouseInfo.objects.filter(type__type_name=info)
            for hi in house_info:
                type_name_list.append(hi.type.type_name)
                user_name_list.append(hi.user.user_name)
            jhouse_info = serializers.serialize('json',house_info)
            return JsonResponse({'jhouse_info': jhouse_info,'type_name_list':type_name_list,'user_name_list':user_name_list})
        elif type==2:
            house_info = HouseInfo.objects.filter(house_address=info)
            for hi in house_info:
                type_name_list.append(hi.type.type_name)
                user_name_list.append(hi.user.user_name)
            jhouse_info = serializers.serialize('json', house_info)
            return JsonResponse(
                {'jhouse_info': jhouse_info, 'type_name_list': type_name_list, 'user_name_list': user_name_list})


class Index_house_add(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'house_add.html')

    def post(self, request, *args, **kwargs):
        # print(request.POST.dict())
        a = request.POST.dict()
        # 获取外键对象实例
        housetype_obj = HouseType.objects.get(type_id=a['type'])
        a['type']= housetype_obj
        user_obj = UserInfo.objects.get(user_id=a['user'])
        a['user']= user_obj
        HouseInfo.objects.create(**a)
        return HttpResponse('添加成功')


class Index_house_edit(View):
    def get(self, request, *args, **kwargs):
        ha = request.GET.get('ha')
        ha_obj = HouseInfo.objects.get(house_address=ha)
        return render(request, 'house_edit.html',{'ha_obj':ha_obj})

    def post(self, request, *args, **kwargs):
        a = request.POST.dict()
        # print(a)
        # 获取外键对象实例
        housetype_obj = HouseType.objects.get(type_id=a['type'])
        a['type'] = housetype_obj
        user_obj = UserInfo.objects.get(user_id=a['user'])
        a['user'] = user_obj
        HouseInfo.objects.filter(house_address=a['house_address']).update(**a)
        return HttpResponse('修改成功')


class Index_house_delete(View):
    def get(self, request, *args, **kwargs):
        ha = request.GET.get('ha')
        HouseInfo.objects.get(house_address=ha).delete()
        return HttpResponse('删除成功')