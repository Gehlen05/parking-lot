from django.urls import path

from .views import MovementPOSTAPIView, MovementPUTAPIView, MovementExitPUTAPIView, Movement


urlpatterns = [
    path('movements/', MovementPOSTAPIView.as_view(), name='movements'),
    path('movements/<int:pk>/', MovementPUTAPIView.as_view(), name='movement'),
    path('movements_exit/<int:pk>/', MovementExitPUTAPIView.as_view(), name='movement_exit'),
]
