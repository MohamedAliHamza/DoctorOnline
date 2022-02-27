from django.urls import path, include

from .import views


user_patterns = [
    path('all_admins/',views.ListAdminApi.as_view(), name='all_admins'),

    path('all_doctors/',views.ListDoctorApi.as_view(), name='all_doctors'),

    path('all_patients/',views.ListPatientApi.as_view(), name='all_patients'),

    path('create_admin/',views.CreateAdminApi.as_view(), name='create_admin'),

    path('create_doctor/',views.CreateDoctorApi.as_view(), name='create_doctor'),

]


urlpatterns = [
    path('users/', include(user_patterns)), 
]    