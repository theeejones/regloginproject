from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/viewuser/(?P<friend_id>\d+)$', views.viewuser),
    url(r'^/addfriend/(?P<friend_id>\d+)$', views.addfriend),
    url(r'^/removefriend/(?P<friend_id>\d+)$', views.removefriend)
]