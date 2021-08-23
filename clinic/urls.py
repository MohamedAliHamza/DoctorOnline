from django.urls import path
from .import views

urlpatterns = [
       path('', views.ClinicListView.as_view(), name='clinic-list'),
       path('add/', views.ClinicCreateView.as_view(), name='clinic-create'),
       path('update-delete/', views.ClinicUpdateDeleteView.as_view(), name='clinic-update'),
       #path('', views.ClinicListView.as_view(), name='clinic-list'),
]
