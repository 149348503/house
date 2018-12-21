from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', views.Index_login.as_view()),
    url(r'^main/$', views.index_main),
    url(r'^top/$', views.Index_top.as_view()),
    url(r'^left/$', views.index_left),
    url(r'^left1/$', views.index_left1),
    url(r'^center/$', views.index_center),
    url(r'^customer_list1/$', views.Index_customer_list1.as_view()),
    url(r'^customer_add/$', views.Index_customer_add.as_view()),
    url(r'^customer_edit/$', views.Index_customer_edit.as_view()),
    url(r'^customer_detail/$', views.Index_customer_detail.as_view()),
    url(r'^customer_delete/$', views.Index_customer_delete.as_view()),
    url(r'^customer_distribute_list/$', views.Index_customer_distribute_list.as_view()),
    url(r'^loginemail/$', views.index_loginemail),
]
