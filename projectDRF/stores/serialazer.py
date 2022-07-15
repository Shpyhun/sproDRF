from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Store


class CalculatorSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=["minus", "plus", "multiply", "divide"])
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()

    def validate(self, data):
        if data['action'] == 'divide' and data['number2'] == 0:
            raise ValidationError("Can't divide by zero")
        return data


class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('name', 'description', 'rating', 'id', 'owner', 'status')
        read_only_fields = ('owner',)
