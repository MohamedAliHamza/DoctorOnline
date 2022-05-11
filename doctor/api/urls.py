from django.urls import path

from .import views


app_name = 'doctor'


urlpatterns = [
    path('doctor/create/',views.CreateDoctorApi.as_view(), name='create'),

    path('doctor/update/',views.UpdateDoctorApi.as_view(), name='update'),
]
