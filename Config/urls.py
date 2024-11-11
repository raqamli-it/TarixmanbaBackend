from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
# for swaggger
from django.conf.urls.static import static
# from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Episyche Technologies",
        default_version='v1',),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('admin_panel.urls')),
    path('api/', include('api.urls')),
    path('user/', include('user.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('ckeditor/', include('ckeditor_uploader.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
