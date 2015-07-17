__author__ = 'MatthewHan'
from django.conf.urls import patterns, url
from apps.ninjas import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<color>[\w-]+)', views.show, name='show'),
)
