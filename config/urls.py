from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from config import settings

urlpatterns = [
    path('', include('web_view.urls')),
    path('api/', include('web_api.urls')),
    path('admin/', admin.site.urls),
    url(r'^public/(?P<path>.*)$', serve, {'document_root': settings.PUBLIC_FILE_ROOT}),
]
