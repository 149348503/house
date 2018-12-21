# -*-coding:utf-8-*-
from django.conf.urls import url

from stu2 import views

urlpatterns = [
    url(r'^dept_add/', views.dept_add),

]

