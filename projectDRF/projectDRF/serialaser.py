from rest_framework import serializers


class StoreSerialazer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    rating = serializers.IntegerField()
