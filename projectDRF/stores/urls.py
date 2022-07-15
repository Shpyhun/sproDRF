from rest_framework import routers

from .views import StoreViewSet, MyStoreViewSet, AdminStoreViewSet

router = routers.SimpleRouter()
router.register(r'stores', StoreViewSet, basename='stores')
router.register(r'my_stores', MyStoreViewSet, basename='my_stores')
router.register(r'admin_stores', AdminStoreViewSet, basename='admin_stores')

