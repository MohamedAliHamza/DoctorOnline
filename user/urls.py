from django.urls import path
from . import views

urlpatterns = [
       # URL For Registration
       path('register/', views.UserRegistrationView.as_view(), name='register'),

       # URL For Login
       path('login/doctor/', views.DoctorTokenView.as_view(), name='token_obtain_pair_doctor'),

       path('login/patient/', views.PatientTokenView.as_view(), name='token_obtain_pair_patient'),

       # URL For Get 
       path('info/', views.UserView.as_view(), name='info'),       

       # URL For Update
       path('update/', views.UpdateUserView.as_view(), name='update'),       
]