from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^emp_list/$', views.Index_emp_list.as_view()),
    url(r'^emp_edit/$', views.Index_emp_edit.as_view()),
    url(r'^emp_detail/$', views.Index_emp_detail.as_view()),
    url(r'^emp_delete/$', views.Index_emp_delete.as_view()),
    url(r'^house_list/$', views.Index_house_list.as_view()),
    url(r'^house_add/$', views.Index_house_add.as_view()),
    url(r'^house_edit/$', views.Index_house_edit.as_view()),
    url(r'^house_delete/$', views.Index_house_delete.as_view()),
]