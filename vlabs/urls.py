from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^stream/$', views.computerScience, name="computerScience"),
    url(r'^problemSolving/$', views.problemSolving, name="problemSolving"),
    url(r'^list_of_labs/$', views.totalLabs, name="totalLabs"),
    url(r'^targetaudience/$', views.targetaudience, name="targetaudience"),
    url(r'^topic/$', views.topic, name="topic"),
    url(r'^feedback/$', views.feedback, name="feedback"),
    url(r'^list_of_labs/(?P<name>[\S]+)/?$', views.lab, name="lab"),
    url(r'^task/(?P<name>[\S]+)/?$', views.task, name="task"),
    url(r'^objective/(?P<name>[\S]+)/?$', views.objective, name="objective"),
]