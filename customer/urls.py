from django.urls import path

from .views import CustomerPUTAPIView, CustomersPOSTAPIView

urlpatterns = [
    path('customers/', CustomersPOSTAPIView.as_view(), name='customers'),
    path('customers/<int:pk>/', CustomerPUTAPIView.as_view(), name='customer'),
]
