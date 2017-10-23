from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^registration$', views.registration),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^$', views.index)
]
