from django.urls import include, path
from rest_framework import routers

from core.views import ProductViewSet, UserViewSet, ContactViewSet, SupplierStatisticView,\
    SupplierListCreateAPIView, SupplierUpdateDeleteAPIView


app_name = "core"

router = routers.SimpleRouter()


router.register(r"product", ProductViewSet, basename='product')
router.register(r"user", UserViewSet, basename='user')
router.register(r"contact", ContactViewSet, basename='contact')


urlpatterns = [
    path("", include(router.urls)),
    path('debt', SupplierStatisticView.as_view(), name='debt'),
    path('supplier/', SupplierListCreateAPIView.as_view(), name='supplier_list'),
    path('supplier_update/<int:pk>/', SupplierUpdateDeleteAPIView.as_view(), name='supplier_update_delete'),
]