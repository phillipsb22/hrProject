
from django.conf.urls import url

from . import views
from . import login_view

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test/$', views.test, name='test'),
  url(r'^login/$', views.login, name='login'),
  url(r'^verify/$', views.validate_login, name='validate_login'),
]