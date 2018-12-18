from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', views.index_login),
    url(r'^main/$', views.index_main),
    url(r'^top/$', views.index_top),
    url(r'^left/$', views.index_left),
    url(r'^center/$', views.index_center),
]
