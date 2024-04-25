from django.urls import path, include
from .views import (
    CelularAPIView,
    CelularesViewSet,
    AvaliacoesViewSet,
)
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('celulares', CelularesViewSet)
router.register('avaliacoes', AvaliacoesViewSet)


urlspatterns = [
    path('celular/<int:pk>/', include(router.urls)),
]



