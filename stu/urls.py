from django.conf.urls import url
from stu import views
urlpatterns = [
    url(r'^login/$', views.index_login),
    url(r'^login1/$', views.index_login1),
    url(r'^main/$', views.index_main),
    url(r'^top/$', views.index_top),
    url(r'^left/$', views.index_left),
    url(r'^center/$', views.index_center),
    url(r'^down/$', views.index_down),
    url(r'^customer_care_list/$', views.index_customer_care_list),
    url(r'^customer_care_add/$', views.index_customer_care_add),
    url(r'^customer_care_edit/$', views.customer_care_edit),
    url(r'^customer_care_del/$', views.customer_care_del),
    url(r'^customer_type_list/$', views.index_customer_type_list),
    url(r'^customer_type_add/$', views.customer_type_add),
    url(r'^customer_type_del/$', views.customer_type_del),

]
