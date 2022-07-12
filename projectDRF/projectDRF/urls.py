from django.contrib import admin
from django.urls import path

from homework.views import hello_world, my_name, today, calculator, StoreApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world, name='hello_world'),
    path('my_name/', my_name, name='my_name'),
    path('today/', today, name='today'),
    path('calculator/', calculator, name='calculator'),
    path('stores/', StoreApiView.as_view(), name='stores'),
]
