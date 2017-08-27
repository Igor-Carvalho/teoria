"""Módulo de configuração de urls do projeto."""

from django.conf import settings, urls
from django.conf.urls import static
from django.contrib import admin
from django.views import generic
from inscritos.views import InscritoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('inscritos', InscritoViewSet)

urlpatterns = [
    urls.url(r'^$', generic.RedirectView.as_view(permanent=True, pattern_name='artigos:lista')),
    urls.url(r'^artigos/', urls.include('artigos.urls', namespace='artigos')),
    urls.url(r'^admin/', urls.include(admin.site.urls)),
    urls.url(r'^api/v1/', urls.include(router.urls, namespace='v1')),
]

# media files in development
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        urls.url(r'^__debug__/', urls.include(debug_toolbar.urls))
    ]
