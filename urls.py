from django.conf.urls import url
from . import views

#urlpattern should be handled as a list containing tuples
urlpattern = [
    url(r'^music/$', views.index),
    ]
