from django.urls import path

from .import views


app_name = 'user'


urlpatterns = [
    # path('user/detail/',views.DetailUserApi.as_view(), name='detail_user'),

    path('login/',views.LoginUserApi.as_view(), name='login'),

]
