from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^computerScience/$', views.computerScience, name="computerScience"),
    url(r'^problemSolving/$', views.problemSolving, name="problemSolving"),
]