from django.urls import path
from .views import ResponseChat

urlpatterns = [
    path('', ResponseChat.as_view(), name='response_chat'),
]

