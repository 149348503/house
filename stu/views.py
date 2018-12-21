from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from stu.models import *





def index_main(request):
    return render(request,'main.html')





def index_left(request):
    return render(request,'left.html')


def index_center(request):
    return render(request,'center.html')








class Index_customer_list1(View):
    def get(self,request,*args,**kwargs):
        # 读取数据库customer_info信息
        customer_info = CustomerInfo.objects.filter()
        listlength = customer_info.count()
        return render(request, 'customer_list1.html', {'customer_info': customer_info,'listlength':listlength})
    def post(self,request,*args,**kwargs):
        # 读取数据库customer_info信息
        info = request.POST.get('info')
        type = int(request.POST.get('type'))
        condition_name_list = []
        source_name_list = []
        user_name_list = []
        type_name_list = []
        if type==1:
            customer_info = CustomerInfo.objects.filter(customer_name=info)
            for ci in customer_info:
                 condition_name_list.append(ci.condition.condition_name)
                 source_name_list.append(ci.source.source_name)
                 user_name_list.append(ci.user.user_name)
                 type_name_list.append(ci.type.type_name)
            jCustomer_info = serializers.serialize('json',customer_info)
            return JsonResponse({'customer_info': jCustomer_info,'condition_name_list':condition_name_list,'source_name_list':source_name_list,'user_name_list':user_name_list,'type_name_list':type_name_list})
        elif type==2:
            customer_info = CustomerInfo.objects.filter(condition__condition_name=info)
            for ci in customer_info:
                 condition_name_list.append(ci.condition.condition_name)
                 source_name_list.append(ci.source.source_name)
                 user_name_list.append(ci.user.user_name)
                 type_name_list.append(ci.type.type_name)
            jCustomer_info = serializers.serialize('json', customer_info)
            return JsonResponse({'customer_info': jCustomer_info, 'condition_name_list': condition_name_list,
                                 'source_name_list': source_name_list, 'user_name_list': user_name_list,
                                 'type_name_list': type_name_list})
        elif type==3:
            customer_info = CustomerInfo.objects.filter(source__source_name=info)
            for ci in customer_info:
                 condition_name_list.append(ci.condition.condition_name)
                 source_name_list.append(ci.source.source_name)
                 user_name_list.append(ci.user.user_name)
                 type_name_list.append(ci.type.type_name)
            jCustomer_info = serializers.serialize('json', customer_info)
            return JsonResponse({'customer_info': jCustomer_info, 'condition_name_list': condition_name_list,
                                 'source_name_list': source_name_list, 'user_name_list': user_name_list,
                                 'type_name_list': type_name_list})
        elif type==4:
            customer_info = CustomerInfo.objects.filter(type__type_name=info)
            for ci in customer_info:
                 condition_name_list.append(ci.condition.condition_name)
                 source_name_list.append(ci.source.source_name)
                 user_name_list.append(ci.user.user_name)
                 type_name_list.append(ci.type.type_name)
            jCustomer_info = serializers.serialize('json', customer_info)
            return JsonResponse({'customer_info': jCustomer_info, 'condition_name_list': condition_name_list,
                                 'source_name_list': source_name_list, 'user_name_list': user_name_list,
                                 'type_name_list': type_name_list})
        elif type==5:
            customer_info = CustomerInfo.objects.filter(user__user_name=info)
            for ci in customer_info:
                 condition_name_list.append(ci.condition.condition_name)
                 source_name_list.append(ci.source.source_name)
                 user_name_list.append(ci.user.user_name)
                 type_name_list.append(ci.type.type_name)
            jCustomer_info = serializers.serialize('json', customer_info)
            return JsonResponse({'customer_info': jCustomer_info, 'condition_name_list': condition_name_list,
                                 'source_name_list': source_name_list, 'user_name_list': user_name_list,
                                 'type_name_list': type_name_list})
        else:
            customer_info = CustomerInfo.objects.filter(customer_company=info)
            for ci in customer_info:
                 condition_name_list.append(ci.condition.condition_name)
                 source_name_list.append(ci.source.source_name)
                 user_name_list.append(ci.user.user_name)
                 type_name_list.append(ci.type.type_name)
            jCustomer_info = serializers.serialize('json', customer_info)
            return JsonResponse({'customer_info': jCustomer_info, 'condition_name_list': condition_name_list,
                                 'source_name_list': source_name_list, 'user_name_list': user_name_list,
                                 'type_name_list': type_name_list})


class Index_customer_add(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer_add.html')


    def post(self, request, *args, **kwargs):
        # print(request.POST.dict())
        a = request.POST.dict()
        # 获取外键对象实例
        condition_obj = CustomerCondition.objects.get(condition_id=a['condition'])
        a['condition']= condition_obj
        type_obj = CustomerType.objects.get(type_id=a['type'])
        a['type']= type_obj
        source_obj = CustomerSource.objects.get(source_id=a['source'])
        a['source']= source_obj
        user_obj = UserInfo.objects.get(user_id=a['user'])
        a['user']= user_obj

        CustomerInfo.objects.create(**a)
        return HttpResponse('添加成功')


class Index_customer_edit(View):
    def get(self, request, *args, **kwargs):
        cn = request.GET.get('cn')
        cn_obj = CustomerInfo.objects.get(customer_name=cn)
        return render(request, 'customer_edit.html',{'cn_obj':cn_obj})

    def post(self, request, *args, **kwargs):
        a = request.POST.dict()
        print(a)
        # 获取外键对象实例
        condition_obj = CustomerCondition.objects.get(condition_id=a['condition'])
        a['condition'] = condition_obj
        type_obj = CustomerType.objects.get(type_id=a['type'])
        a['type'] = type_obj
        source_obj = CustomerSource.objects.get(source_id=a['source'])
        a['source'] = source_obj
        user_obj = UserInfo.objects.get(user_id=a['user'])
        a['user'] = user_obj
        a.pop('customer_id')
        CustomerInfo.objects.filter(customer_name=a['customer_name']).update(**a)
        return HttpResponse('修改成功')


class Index_customer_detail(View):
    def get(self, request, *args, **kwargs):
        cn = request.GET.get('cn')
        cn_obj = CustomerInfo.objects.get(customer_name=cn)
        return render(request, 'customer_detail.html',{'cn_obj':cn_obj})


class Index_customer_delete(View):
    def get(self, request, *args, **kwargs):
        cn = request.GET.get('cn')
        CustomerInfo.objects.get(customer_name=cn).delete()
        return HttpResponse('删除成功')


class Index_customer_distribute_list(View):
    def get(self, request, *args, **kwargs):
        customer_info = CustomerInfo.objects.filter()
        listlength = customer_info.count()
        return render(request,'customer_distribute_list.html',{'customer_info':customer_info,'listlength':listlength})
    def post(self, request, *args, **kwargs):
        a = request.POST.dict()
        # 获取分配员工对象实例
        user_obj = UserInfo.objects.get(user_id=a['user'])
        a['user'] = user_obj
        CustomerInfo.objects.filter(customer_name=a['customer_name']).update(**a)
        return HttpResponse('分配成功')


class Index_login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    def post(self, request, *args, **kwargs):
        a = request.POST.dict()
        print(a)
        # 获取分配员工对象实例
        # user_obj = UserInfo.objects.get(user_id=a['user'])
        # a['user'] = user_obj
        # CustomerInfo.objects.filter(customer_name=a['customer_name']).update(**a)
        # 判断用户是否存在
        if UserInfo.objects.filter(user_num=a['user_num'],user_pw=a['user_pw']):
            return render(request,'main.html',{'user_num':a['user_num'],'user_pw':a['user_pw']})
        else:
            return render(request,'error.html')


class Index_top(View):
    def get(self, request, *args, **kwargs):
        user_num = request.GET.get('user_num')
        user_obj = UserInfo.objects.get(user_num=user_num)
        return render(request, 'top.html',{'user_obj':user_obj})


def index_loginemail(request):
    return render(request,'loginemail.html')