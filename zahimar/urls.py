from django.urls import path
from .views import *
from . import api
from django.conf import settings
from django.conf.urls.static import static

app_name = 'zahimar'


urlpatterns = [
    path('prediction/', api.ZahimarApi.as_view(), name='prediction'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)