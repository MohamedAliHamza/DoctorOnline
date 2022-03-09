from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin


# apps_patterns = [
#     # User
#     path('', include('user.api.urls')),
    

# ]

urlpatterns = [
    path('', include('user.urls')),
    
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
