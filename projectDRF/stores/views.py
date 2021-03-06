from datetime import datetime

from rest_framework import filters
from rest_framework.decorators import api_view, action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend


from .models import Store
from .serialazer import CalculatorSerializer, StoreSerializer


@api_view(http_method_names=['GET'])
def hello_world(request):
    return_dict = {'msg': 'Hello World'}
    return Response(return_dict)


@api_view(http_method_names=['GET'])
def my_name(request):
    return_name = {'name': 'Volodymyr Shpygun'}
    return Response(return_name)


@api_view(http_method_names=['GET'])
def today(request):
    date = datetime.now()
    return_date = {'date': date.strftime('%d/%m/%Y'),
                   'year': date.strftime('%Y'),
                   'month': date.strftime('%m'),
                   'day': date.strftime('%d')
                   }
    return Response(return_date)


@api_view(http_method_names=['POST'])
def calculator(request):
    data = request.data
    serializer = CalculatorSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    operation = serializer.validated_data
    if operation['action'] == "plus":
        res = operation['number1'] + operation['number2']
    elif operation['action'] == 'minus':
        res = operation['number1'] - operation['number2']
    elif operation['action'] == 'divide':
        res = operation['number1'] / operation['number2']
    elif operation['action'] == 'multiply':
        res = operation['number1'] * operation['number2']
    return Response({"Result": res})


class StoreApiView(APIView):

    def get(self, request, format=None):
        """
        Return a list of all stores
        """
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new store
        """
        serializer = StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_201_CREATED, data=serializer.data)


class StoreViewSet(ListModelMixin,
                   RetrieveModelMixin,
                   GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class MyStoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(**{'owner': self.request.user})

    @action(methods=['post'], detail=True)
    def set_mark_as_active(self, request, pk=None):
        """
        Changes the store status from deactivated to active
        """
        store = self.get_object()
        if store.status == 'deactivated':
            store.status = 'active'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def set_mark_as_deactivated(self, request, pk=None):
        """
        Changes the store status from active to deactivated
        """
        store = self.get_object()
        if store.status == 'active':
            store.status = 'deactivated'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)


class AdminStoreViewSet(ListModelMixin,
                        RetrieveModelMixin,
                        GenericViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['name']
    ordering_fields = ['rating']

    @action(methods=['post'], detail=True)
    def set_mark_as_active(self, request, pk=None):
        """
        Changes the store status from in_review to active
        """
        store = self.get_object()
        if store.status == 'in_review':
            store.status = 'active'
            store.save()
        serializer = self.get_serializer(store)
        return Response(serializer.data)
