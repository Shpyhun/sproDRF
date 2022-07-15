from django.contrib import admin
from django.urls import path, include

from stores.views import hello_world, today, my_name, calculator, StoreViewSet, MyStoreViewSet, AdminStoreViewSet
from stores.urls import router as store_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world, name='hello_world'),
    path('my_name/', my_name, name='my_name'),
    path('today/', today, name='today'),
    path('calculator/', calculator, name='calculator'),
    path('', include(store_router.urls), name='stores'),
    path('', include(store_router.urls), name='my_store'),
    path('', include(store_router.urls), name='admin_store'),
]
