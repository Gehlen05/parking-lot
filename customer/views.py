from rest_framework import generics


from .models import Customer
from .serializers import CustomerSerializer


class CustomersPOSTAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerPUTAPIView(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
