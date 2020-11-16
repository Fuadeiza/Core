from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('admin/', admin.site.urls),
    path('',include("core.urls")),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)