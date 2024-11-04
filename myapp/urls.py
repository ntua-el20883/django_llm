from django.urls import path
from .views import QAPIView, chat_view, test_view

urlpatterns = [
    path('test/', test_view, name='test'),
    path('api/qa/', QAPIView.as_view(), name='qa'),
    path('chat/', chat_view, name='chat'),
]