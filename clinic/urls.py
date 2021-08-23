from django.urls import path
from .import views

urlpatterns = [
       path('clinic/', views.ClinicListView.as_view(), name='clinic-list'),
       path('clinic/add/', views.ClinicCreateView.as_view(), name='clinic-create'),
       path('clinic/update/', views.ClinicUpdateDeleteView.as_view(), name='clinic-update'),
       #path('', views.ClinicListView.as_view(), name='clinic-list'),
]
