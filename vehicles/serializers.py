from rest_framework import serializers

from .models import Vehicle


class VehiclesSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField()

    class Meta:
        model = Vehicle
        fields = (
            'id',
            'customer_id',
            'plate',
            'kind'
        )
