from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # Apps URL
    path('api/v1/', include('user.urls')),
    path('api/v1/', include('clinic.urls')),
    path('api/v1/', include('reservation.urls')),
    path('admin/', admin.site.urls),
    
    # Docs URL
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),

]
