from rest_framework import serializers

from .models import Movement


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = (
            'id',
            'vehicle',
            'entry_date',
            'plate',
        )


class MovementExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = (
            'id',
            'vehicle',
            'exit_date',
            'validate_date',
            'value_real',
            'plate',
        )
