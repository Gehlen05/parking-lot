from django.urls import path

from .views import VehiclesPOSTAPIView, VehiclesPUTAPIView


urlpatterns = [
    path('vehicles/', VehiclesPOSTAPIView.as_view(), name='vehicles'),
    path('vehicles/<int:pk>/', VehiclesPUTAPIView.as_view(), name='vehicle'),
]
