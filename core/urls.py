from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    # path('reservation/', include('reservation.urls')),
    # path('', include('user.urls')),
    # path('', include('patient.urls')),
    # path('', include('utility.urls')),
    
    path('admin/', admin.site.urls,),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

