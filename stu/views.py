# coding=utf-8
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
from django.core import serializers
# Create your views here.
def index_login(request):
    return render(request,'login.html')

def index_login1(request):
    return render(request,'login1.html')


def index_main(request):
    return render(request,'main.html')


def index_top(request):
    return render(request,'top.html')


def index_left(request):
    return render(request,'left.html')

def index_center(request):
    return render(request,'center.html')


def index_down(request):
    return render(request,'down.html')


import jsonpickle
# 查询客户关怀内容
def index_customer_care_list(request):
    content=request.GET.get('content','')
    type=request.GET.get('type','')
    if type=='1':
        # 获取所有
        qcustomer_care_list1 = CustomerInfo.objects.filter(customer_name=content)
        if qcustomer_care_list1:
            qcustomer_care_list_name=CustomerInfo.objects.values('customer_name').filter(customer_name=content)
            for q in qcustomer_care_list1:
                qcustomer_care_list=q.customercare_set.all()
            qlist = [jsonpickle.dumps(q, unpicklable=False) for q in qcustomer_care_list_name if q]

            #存储
            jcustomer_care_list = serializers.serialize('json', qcustomer_care_list)
            # print(qlist)
            # print(jcustomer_care_list)
            return JsonResponse({'jcustomer_care_list': jcustomer_care_list,'qlist':qlist,'flag':True})
        return JsonResponse({'flag':False})
    elif type=='2':
        # 获取关怀表对象集合

        qcustomer_care_list=CustomerCare.objects.filter(care_theme=content)
        if qcustomer_care_list:
            qlist1 = []
            for i in qcustomer_care_list:
                qlist1.append(i.customer)
            qlist = [jsonpickle.dumps(q, unpicklable=False) for q in qlist1 if q]
            jcustomer_care_list=serializers.serialize('json',qcustomer_care_list)
            # qlist=serializers.serialize('json',qlist1)
            return JsonResponse({'jcustomer_care_list':jcustomer_care_list,'qlist':qlist,'flag':True})
        return JsonResponse({'flag':False})

    elif type=='3':

        qcustomer_care_list = CustomerCare.objects.filter(care_way=content)
        if qcustomer_care_list:
            qlist1 = []
            for i in qcustomer_care_list:
                qlist1.append(i.customer)
            qlist = [jsonpickle.dumps(q, unpicklable=False) for q in qlist1 if q]
            jcustomer_care_list = serializers.serialize('json', qcustomer_care_list)
            # qlist=serializers.serialize('json',qlist1)
            return JsonResponse({'jcustomer_care_list': jcustomer_care_list, 'qlist': qlist,'flag':True})
        return JsonResponse({'flag':False})
    customer_care_list=CustomerCare.objects.all()
    return render(request,'customer_care_list.html',{'customer_care_list':customer_care_list})



# 添加客户关怀表
def index_customer_care_add(request):
    if request.method=='GET':
        customerinfolist=CustomerInfo.objects.all()

        return render(request,'customer_care_add.html',{'customerinfolist':customerinfolist})
    else:
        # 获取输入框的数据
        careTheme=request.POST.get('careTheme','')
        careNexttime=request.POST.get('careNexttime','')
        carePeople=request.POST.get('carePeople','')
        customerId=request.POST.get('customerId','')
        careWay=request.POST.get('careWay','')
        careRemark=request.POST.get('careRemark','')
        # 添加数据
        CustomerCare.objects.create(customer_id=customerId,care_theme=careTheme,care_nexttime=careNexttime,
                                    care_people=carePeople,care_way=careWay,care_remark=careRemark,is_used=1)

        return HttpResponseRedirect('/stu/customer_care_list')

# 客户关怀编辑
def customer_care_edit(request):
    if request.method == 'GET':
        num=request.GET.get('num','')
        num=int(num)

        customerinfolist = CustomerInfo.objects.all()
        customercarelistall = CustomerCare.objects.all()
        list1=[]
        for i in customercarelistall:
            # print(i.care_way)
            list1.append(i.care_way)
        list1=list(set(list1))

        customercarelist = CustomerCare.objects.get(care_id=num)
        return render(request, 'customer_care_edit.html',{'customercarelist':customercarelist,'customerinfolist':customerinfolist,'customercarelistall':list1})
    else:
        # 获取输入框的数据
        careId = request.POST.get('careId', '')

        print(careId)
        careTheme = request.POST.get('careTheme', '')
        careNexttime = request.POST.get('careNexttime', '')
        carePeople = request.POST.get('carePeople', '')
        customerId = request.POST.get('customerId', '')
        careWay = request.POST.get('careWay', '')
        careRemark = request.POST.get('careRemark', '')
        # 添加数据
        CustomerCare.objects.filter(care_id=careId).update(customer_id=customerId, care_theme=careTheme, care_nexttime=careNexttime,
                                    care_people=carePeople, care_way=careWay, care_remark=careRemark, is_used=1)
    return HttpResponseRedirect('/stu/customer_care_list/')

# 客户关怀删除
def customer_care_del(request):
    num=request.GET.get('num','')
    num=int(num)
    CustomerCare.objects.filter(care_id=num).delete()
    return HttpResponseRedirect('/stu/customer_care_list')
# 客户类型
def index_customer_type_list(request):
    if request.method=='GET':
        customer_type_list = CustomerType.objects.all()
        return render(request, 'customer_type_list.html', {'customer_type_list': customer_type_list})
    else:
        typename = request.POST.get('typename', '')

        customer_type_list = CustomerType.objects.filter(type_name=typename)
        if customer_type_list:
            return render(request,'customer_type_list.html',{'customer_type_list':customer_type_list})
        else:
            return HttpResponseRedirect('/stu/customer_type_list/')


# 客户类型添加
def customer_type_add(request):
    if request.method=='GET':

        return render(request,'customer_type_add.html')
    else:
        typeName=request.POST.get('typeName','')
        CustomerType.objects.create(type_name=typeName,is_used=1)
        # return HttpResponse(u'添加成功')
        return HttpResponseRedirect('/stu/customer_type_list/')


# 客户类型删除
def customer_type_del(request):

    num=request.GET.get('num','')
    num=int(num)
    if num==1 or num==2 or num==3:
        return HttpResponse(u'不能删除，没有权限')
    else:
        CustomerType.objects.filter(type_id=num).delete()
        return HttpResponseRedirect('/stu/customer_type_list/')