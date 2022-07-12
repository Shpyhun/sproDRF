from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

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
