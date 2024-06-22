from django.urls import include, path
from rest_framework import routers
from .views import MarcaViewSet, DueñoViewSet, CarViewSet, DueñoCarViewSet

router = routers.DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'dueños', DueñoViewSet)
router.register(r'cars', CarViewSet)
router.register(r'dueño-cars', DueñoCarViewSet)

urlpatterns = [
    path("api/v1/", include (router.urls))
]   