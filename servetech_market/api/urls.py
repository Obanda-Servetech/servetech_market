from django.urls import path, include
from rest_framework import routers
from .views import (
    CustomerViewSet, CategoryViewSet, ProductViewSet, 
    OrderViewSet, OrderItemViewSet
)

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orders/(?P<order_id>[^/.]+)/items', OrderItemViewSet, basename='order-items')

urlpatterns = [
    path('', include(router.urls)),
]
