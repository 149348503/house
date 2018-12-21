#coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from stu.models import *
# Create your views here.
# 部门信息展示
def dept_list(request):
    if request.method=='GET':
        dept_list= DepartmentInfo.objects.all()
        return render(request,'dept_list.html',{'dept_list':dept_list})
    else:
        departmentName=request.POST.get('departmentName','')

        dept_list=DepartmentInfo.objects.filter(department_name=departmentName)
        if dept_list:
            return render(request,'dept_list.html',{'dept_list':dept_list})
        else:
            return HttpResponseRedirect('/stu1/dept_list/')

# 部门信息删除
def dept_list_del(request):
    num=request.GET.get('num','')
    num=int(num)
    if num==1 or num==3:
        return HttpResponse(u'没有权限')


    else:
        DepartmentInfo.objects.filter(department_id=num).delete()

        return HttpResponseRedirect('/stu1/dept_list/')


# 公告信息展示
def notice_list(request):
    if request.method=='GET':

        noticeinfolist=NoticeInfo.objects.all()
        return render(request,'notice_list.html',{'noticeinfolist':noticeinfolist})
    else:
        noticeInput=request.POST.get('noticeInput','')
        queryType=request.POST.get('queryType','')
        if queryType=='1':
            noticeinfolist=NoticeInfo.objects.filter(notice_item=noticeInput)
            return render(request, 'notice_list.html', {'noticeinfolist': noticeinfolist})
        elif queryType=='2':
            noticeinfolist = NoticeInfo.objects.filter(notice_content=noticeInput)
            return render(request, 'notice_list.html', {'noticeinfolist': noticeinfolist})

# 公告添加
def notice_list_add(request):
    if request.method=='GET':
        userinfolist=UserInfo.objects.all()
        return render(request,'notice_list_add.html',{'userinfolist':userinfolist})
    else:
        notice_item=request.POST.get('notice_item','')
        user_id=request.POST.get('user_id','')
        notice_time=request.POST.get('notice_time','')
        notice_endtime=request.POST.get('notice_endtime','')
        notice_content=request.POST.get('notice_content','')
        NoticeInfo.objects.create(user_id=user_id,notice_item=notice_item,
                                  notice_time=notice_time,notice_endtime=notice_endtime,notice_content=notice_content,is_used=1)

        return HttpResponseRedirect('/stu1/notice_list/')

# 公告删除
def notice_list_del(request):
    num=request.GET.get('num','')
    num=int(num)
    NoticeInfo.objects.filter(notice_id=num).delete()
    return  HttpResponseRedirect('/stu1/notice_list/')