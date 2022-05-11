from django.urls import path

from .import views


app_name = 'patient'


urlpatterns = [
    path('patient/create/',views.CreatePatientApi.as_view(), name='create'),

    path('patient/update/',views.UpdatePatientApi.as_view(), name='update'),
]
