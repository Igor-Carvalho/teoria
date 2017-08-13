"""Módulo de configuração de urls do projeto."""

from artigos.views import ArtigoVisões
from core.views import UserViewSet
from django.conf import settings, urls
from django.conf.urls import static
from django.contrib import admin
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('artigos', ArtigoVisões)

urlpatterns = [
    urls.url(r'^$', views.IndexView.as_view(), name='index'),
    urls.url(r'^api/v1/', urls.include(router.urls, namespace='v1')),
    urls.url(r'^admin/', urls.include(admin.site.urls)),
]

# media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        urls.url(r'^__debug__/', urls.include(debug_toolbar.urls))
    ]
