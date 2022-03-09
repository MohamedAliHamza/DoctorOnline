from django.urls import path, include

from .import views


user_patterns = [
    # path('create/',views.CreatePatientView.as_view(), name='create'),

    # path('update/',views.UpdateUserApi.as_view(), name='update'),

    # path('detail/',views.DetailUserApi.as_view(), name='detail'),
    path('', views.home_view)
]


urlpatterns = [    

    path('users/', include(user_patterns)),
]
