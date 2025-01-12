from django.urls import path
from core.application.api import get_api


urlpatterns = [
    path('', get_api().urls)
]