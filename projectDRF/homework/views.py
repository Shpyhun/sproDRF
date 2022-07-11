from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

from projectDRF.serialazer import CalculatorSerializer


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

