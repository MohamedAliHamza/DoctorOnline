from django.urls import path, include

from .import views


urlpatterns = [

    path('create_admin/',views.CreateAdminApi.as_view(), name='create_admin'),

    path('update_admin/',views.UpdateAdminApi.as_view(), name='update_admin'),

    path('admins_list/',views.ListAdminApi.as_view(), name='admins_list'),

    path('customers/',views.ListCustomerApi.as_view(), name='customers_list'),

]
   