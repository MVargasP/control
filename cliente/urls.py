from django.urls import path, include
from django.conf import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
	path('',ConsultaView.as_view(),name='consulta'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
