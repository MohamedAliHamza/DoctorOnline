from django.urls import path
from .import views

urlpatterns = [
       # URL For List Clinic 
       path('', views.ClinicListView.as_view(), name='list-clinic'),
       # URL For Create Clinic
       path('add/', views.ClinicCreateView.as_view(), name='clinic-create'),
       # URL For Updated Retrieve Update Destroy Clinic
       path('update/<int:pk>/', views.ClinicUpdateDeleteView.as_view(), name='update-clinic'),
       # URL List Clinic For Specific Doctor
       path('doctor/', views.ClinicDoctorosListView.as_view(), name='list-clinic-doctor'),

]
