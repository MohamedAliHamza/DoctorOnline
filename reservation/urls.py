from django.urls import path
from . import views

urlpatterns = [
       # URL For List Reservation For Specific User 
       path('', views.ListReservationView.as_view(), name='list-reservation'),
       # URL For Add Reservation
       path('add/', views.CreateReservationView.as_view(), name='add-reservation'),
       # URL For Updated Retrieve Update Destroy Reservation
       path('update/<int:pk>/', views.UpdateDeleteReservationView.as_view(), name='update-reservation')
]
 