from django.urls import path

from .import views


app_name = 'doctor_report'


urlpatterns = [
    path('doctor/report/create/',views.CreateReportApi.as_view(), name='create'),

    # path('doctor/report/list/',views.UpdatePatientApi.as_view(), name='list'),
]
