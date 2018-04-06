from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'hms'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^patientsindex/$', views.PatientIndex.as_view()),
    url(r'^doctorsindex/$', views.DoctorIndex.as_view()),
    url(r'^appointmentsindex/$', views.AppointmentIndex.as_view()),
    url(r'^tipsindex/$', views.TipsIndex.as_view()),
]

