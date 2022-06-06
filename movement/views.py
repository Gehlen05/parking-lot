from rest_framework import generics
from datetime import datetime

from django.utils import timezone
from .models import Movement
from .serializers import MovementSerializer, MovementExitSerializer


class MovementPOSTAPIView(generics.ListCreateAPIView):
    Movement.entry_date = datetime.now(tz=timezone.utc)
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer


class MovementPUTAPIView(generics.RetrieveUpdateAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementSerializer


class MovementExitPUTAPIView(generics.RetrieveUpdateAPIView):
    queryset = Movement.objects.all()
    serializer_class = MovementExitSerializer
