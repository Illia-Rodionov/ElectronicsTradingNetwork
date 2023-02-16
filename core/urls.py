from django.urls import include, path
from rest_framework import routers

from core.views import SupplierViewSet, ProductViewSet, UserViewSet, ContactViewSet, SupplierStatisticView

app_name = "core"

router = routers.SimpleRouter()

router.register(r"supplier", SupplierViewSet, basename='supplier')
router.register(r"product", ProductViewSet, basename='product')
router.register(r"user", UserViewSet, basename='user')
router.register(r"contact", ContactViewSet, basename='contact')


urlpatterns = [
    path("", include(router.urls)),
    path('debt', SupplierStatisticView.as_view(), name='debt'),
]