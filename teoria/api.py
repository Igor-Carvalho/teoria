"""API routes."""

from inscritos.api import InscritoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('inscritos', InscritoViewSet)

urls = router.urls, 'teoria', 'v1'
