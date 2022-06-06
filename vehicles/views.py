from rest_framework import generics


from .models import Vehicle
from .serializers import VehiclesSerializer


class VehiclesPOSTAPIView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehiclesSerializer


class VehiclesPUTAPIView(generics.RetrieveUpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehiclesSerializer
