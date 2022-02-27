from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView

from .import views


user_patterns = [
    path('create/',views.CreatePatientApi.as_view(), name='create'),

    path('update/',views.UpdateUserApi.as_view(), name='update'),

    path('detail/',views.DetailUserApi.as_view(), name='detail'),
]


urlpatterns = [    
    path('login/', TokenObtainPairView.as_view(), name='login'),

    path('users/', include(user_patterns)),
]
