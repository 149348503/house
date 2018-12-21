# -*-coding:utf-8-*-
from django.conf.urls import url
from stu1 import views

urlpatterns = [

    url(r'^dept_list/',views.dept_list),
    url(r'^dept_list_del/',views.dept_list_del),
    url(r'^notice_list/',views.notice_list),
    url(r'^notice_list_add/',views.notice_list_add),
    url(r'^notice_list_del/',views.notice_list_del),

]