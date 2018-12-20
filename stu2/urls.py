from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^emp_add/$', views.Index_emp_add.as_view()),

]