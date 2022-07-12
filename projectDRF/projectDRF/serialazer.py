from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from homework.models import Store


class CalculatorSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=["minus", "plus", "multiply", "divide"])
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()

    def validate(self, data):
        if data['action'] == 'divide' and data['number2'] == 0:
            raise ValidationError("Can't divide by zero")
        return data


class StoreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=800)
    rating = serializers.IntegerField(min_value=1, max_value=100)

    def create(self, validated_data):
        store = Store.objects.create(**validated_data)
        return store
