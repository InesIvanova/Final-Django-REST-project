from django.urls import path, re_path

from . import views

urlpatterns = [
    path("appointments/", views.AppointmentList.as_view()),
    re_path('^appointments/(?P<pk>\d+)/$', views.AppointmentDetail.as_view()),
]
