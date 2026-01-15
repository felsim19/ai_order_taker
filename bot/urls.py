from .views import OrderBotView
from django.urls import path

urlpatterns = [
    path('chat/', OrderBotView.as_view(), name='bot-chat'),
]